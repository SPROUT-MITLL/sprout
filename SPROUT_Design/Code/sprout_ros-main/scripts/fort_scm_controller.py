#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy
from std_msgs.msg import Bool
from threading import Lock
from fort_scm import (
    ScmSerial,
    MessageControl,
    UserValue,
    Joystick,
    SetUserValue,
    GetUserValue,
    UserFeedbackValueKeys,
    UserFeedbackStringKeys,
    UserFeedbackDisplayModes,
    SetUserNameString
)
from sprout_ros.msg import State
from sprout_ros.srv import PressureSet


SCM_PORT = "/dev/input/fort"
JOY_RATE_HZ = 100
AXIS_SCALE = 1023.0
READ_TIMEOUT_SEC = 0.01
READ_USER_VARIABLE_RATE_HZ = 1

class FortSCMJoyNode(Node):
    def __init__(self):
        super().__init__("fort_scm_joy")

        self.joy_pub = self.create_publisher(Joy, "/joy", 1)
        self.status_pub = self.create_publisher(Bool, "/joy/status", 1)
        self.scm = None
        self.connected = False
        self.connect()
        self.lock = Lock()
        # Create clients
        self.pressure_set_client = self.create_client(
            PressureSet,
            '/pressure_set',
        )
        self.timer = self.create_timer(READ_TIMEOUT_SEC, self.read_joystick)
        self.user_val_timer = self.create_timer(READ_USER_VARIABLE_RATE_HZ, self.read_all_user_variables)
        # Subscribe to the state so we can write things back to the screen
        self.set_display_mode()
        self.sub = self.create_subscription(State, '/vine_state', self.update_display, 1)

    def set_display_mode(self):
        """
        Set the display mode on the controller to be able to write custom values to it.
        """
        self.scm.write(
            SetUserValue(
                UserFeedbackValueKeys.DISPLAY_MODE, UserFeedbackDisplayModes.USERTEXT
            )
        )
        # set user variable names
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.USERVALUE1, "Max Chamb PSI"))
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.USERVALUE2, "Max Pouch PSI"))

    def publish_status(self, state: bool):
        if self.connected == state:
            return
        self.connected = state
        msg = Bool()
        msg.data = state
        self.status_pub.publish(msg)

    def update_display(self, msg: State):
        """
        This function should write core values about the screen display to the controller including:
        Chamber Pressure vs. Max Pressure
        Actuator Pressure(s) vs. Max Pressures
        Length of robot
        Growth Rates
        Any warnings

        This function should run at some frequency, perhaps 1-5 Hz, to ensure the display is updated in a timely manner. 
        It should also be called whenever there is a significant change in the values being displayed (e.g. max pressure changes, growth rate changes, etc.)
        This needs to have access to the vine state topic 
        """
        if msg is None:
            return
        status = 'Okay'  # or derive from msg if needed
        line0 = f"{status} Main:{msg.cp_s:.2f}//{msg.c_m:.2f}"
        line1 = f"Act #1: {msg.a1_s:.2f}//{msg.a_m:.2f}"
        line2 = f"Act #2: {msg.a2_s:.2f}//{msg.a_m:.2f}"
        line3 = f"Act #3: {msg.a3_s:.2f}//{msg.a_m:.2f}"

        self.get_logger().debug(f"LCD Update:\n{line0}\n{line1}\n{line2}\n{line3}")
        # Write to the display variables on the controller
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.CUSTOMTEXTLINE1, line0))
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.CUSTOMTEXTLINE2, line1))
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.CUSTOMTEXTLINE3, line2))
        self.scm.write(SetUserNameString(UserFeedbackStringKeys.CUSTOMTEXTLINE4, line3))


    def update_pressures(self, chamber_pressure: float, pouch_pressure: float):
        """
        Asynchronously update the maximum pressures allowed by the base.
        """
        if not self.pressure_set_client.service_is_ready():
            self.get_logger().warn("Pressure set service not available")
            return

        req = PressureSet.Request()
        req.chamber_val = chamber_pressure
        req.actuator_val = pouch_pressure
        future = self.pressure_set_client.call_async(req)
        future.add_done_callback(self.handle_pressure_set_response)

    def handle_pressure_set_response(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")
            return

        if not response.success:
            self.get_logger().warn(
                "Failed to set new pressures!"
            )
            return

    def read_user_variable(self, key: UserFeedbackValueKeys):
        """
        Stub: Read a user feedback variable from the controller.

        Args:
            key: UserFeedbackValueKeys enum identifying the variable

        Returns:
            None for now. Will eventually return the decoded value.
        """
        if self.scm is None:
            self.get_logger().debug("SCM not connected, cannot read user variable")
            return None

        self.get_logger().debug(
            f"read_user_variable called for key={key.name} (stub)"
        )
        with self.lock:
            # Retrieve the value and compare
            self.scm.write(GetUserValue(key))
            result = self.scm.wait_for_message(UserValue)
            # Add some logic checks here.....
            return result

    def read_all_user_variables(self):
        """
        Stub: Read all relevant user variables from the controller.

        Intended to be used for:
        - Initial sync on connect
        - Debug / diagnostics
        - Periodic polling if needed
        """
        if self.scm is None:
            return

        self.get_logger().debug("read_all_user_variables")
        # Read Max Chamber Pressure
        chamber_pressure = self.read_user_variable(UserFeedbackValueKeys.CUSTOM1)
        # Read Max Pouch Pressure
        actuator_pressure = self.read_user_variable(UserFeedbackValueKeys.CUSTOM2)
        # Call service to update values on base
        self.update_pressures(float(chamber_pressure.value), float(actuator_pressure.value))
        # print(chamber_pressure.value)
        # print(actuator_pressure.value)


    def connect(self):
        try:
            self.scm = ScmSerial(SCM_PORT)
            self.scm.write(MessageControl(Joystick, True, JOY_RATE_HZ))
            self.get_logger().info("Connected to Fort SCM joystick")
            self.publish_status(True)
        except Exception as e:
            self.get_logger().error(f"Failed to connect to SCM: {e}")
            self.scm = None
            self.publish_status(False)

    def disconnect(self, reason: str):
        if self.scm:
            try:
                self.scm.close()
            except Exception:
                pass

        self.get_logger().warn(f"SCM disconnected: {reason}")
        self.scm = None
        self.publish_status(False)

    def read_joystick(self):
        with self.lock:
            if self.scm is None:
                return
            try:
                js = self.scm.wait_for_message(Joystick, timeout=READ_TIMEOUT_SEC)
            except Exception as e:
                self.disconnect(str(e))
                return

            if not js:
                return

            if js.errors:
                self.get_logger().warn_once(
                    f"Joystick message contained errors: {js.errors}"
                )

            msg = Joy()

            msg.axes = [
                js.left_x / AXIS_SCALE,
                js.left_y / AXIS_SCALE,
                js.left_z / AXIS_SCALE,
                js.right_x / AXIS_SCALE,
                js.right_y / AXIS_SCALE,
                js.right_z / AXIS_SCALE,
            ]

            # Button order is explicit and stable
            msg.buttons = [
                int(Joystick.Button.UP in js.left_buttons),
                int(Joystick.Button.RIGHT in js.left_buttons),
                int(Joystick.Button.DOWN in js.left_buttons),
                int(Joystick.Button.LEFT in js.left_buttons),
                int(Joystick.Button.DOWN in js.right_buttons),   # 1
                int(Joystick.Button.RIGHT in js.right_buttons),  # 2
                int(Joystick.Button.UP in js.right_buttons),     # 3
                int(Joystick.Button.LEFT in js.right_buttons),   # 4
            ]

            self.joy_pub.publish(msg)

    def destroy_node(self):
        if self.scm:
            try:
                self.scm.close()
            except Exception:
                pass
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = FortSCMJoyNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
