---
layout: null
---
// Click-to-load 3D preview for STEP files, used on the CAD pages.
// Parses STEP geometry client-side with occt-import-js (OpenCascade/WASM)
// and renders it with three.js + OrbitControls.

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const OCCT_JS_URL = '{{ site.baseurl }}/assets/vendor/occt-import-js/occt-import-js.js';

let occtModulePromise = null;

function loadOcctModule() {
  if (occtModulePromise) return occtModulePromise;
  occtModulePromise = new Promise((resolve, reject) => {
    if (window.occtimportjs) {
      resolve(window.occtimportjs());
      return;
    }
    const script = document.createElement('script');
    script.src = OCCT_JS_URL;
    script.onload = () => resolve(window.occtimportjs());
    script.onerror = () => reject(new Error('Could not load the STEP parser.'));
    document.head.appendChild(script);
  });
  return occtModulePromise;
}

function buildModelGroup(occtResult) {
  const group = new THREE.Group();
  for (const mesh of occtResult.meshes) {
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.Float32BufferAttribute(mesh.attributes.position.array, 3));
    if (mesh.attributes.normal) {
      geometry.setAttribute('normal', new THREE.Float32BufferAttribute(mesh.attributes.normal.array, 3));
    }
    geometry.setIndex(Array.from(mesh.index.array));
    if (!mesh.attributes.normal) {
      geometry.computeVertexNormals();
    }
    const color = mesh.color
      ? new THREE.Color(mesh.color[0], mesh.color[1], mesh.color[2])
      : new THREE.Color(0x9aa5b1);
    const material = new THREE.MeshStandardMaterial({ color, metalness: 0.1, roughness: 0.7, side: THREE.DoubleSide });
    group.add(new THREE.Mesh(geometry, material));
  }
  return group;
}

function frameCamera(object, camera, controls) {
  const box = new THREE.Box3().setFromObject(object);
  const size = box.getSize(new THREE.Vector3());
  const center = box.getCenter(new THREE.Vector3());
  const maxDim = Math.max(size.x, size.y, size.z) || 1;
  const distance = maxDim * 2.2;
  camera.near = maxDim / 100;
  camera.far = maxDim * 100;
  camera.position.set(center.x + distance, center.y + distance * 0.7, center.z + distance);
  camera.updateProjectionMatrix();
  controls.target.copy(center);
  controls.update();
}

function renderModel(container, occtResult) {
  const canvasHolder = container.querySelector('.step-viewer-canvas');
  const width = canvasHolder.clientWidth;
  const height = canvasHolder.clientHeight || 400;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xf5f6fa);

  const camera = new THREE.PerspectiveCamera(45, width / height, 0.01, 1000);

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setSize(width, height);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  canvasHolder.appendChild(renderer.domElement);

  scene.add(new THREE.HemisphereLight(0xffffff, 0x444444, 1.2));
  const dirLight = new THREE.DirectionalLight(0xffffff, 1.1);
  dirLight.position.set(1, 2, 3);
  scene.add(dirLight);

  const model = buildModelGroup(occtResult);
  scene.add(model);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  frameCamera(model, camera, controls);

  const resizeObserver = new ResizeObserver(() => {
    const w = canvasHolder.clientWidth;
    const h = canvasHolder.clientHeight || 400;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  });
  resizeObserver.observe(canvasHolder);

  function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
  }
  animate();
}

function initStepViewer(container) {
  const url = container.dataset.stepUrl;
  const button = container.querySelector('.step-viewer-load');
  const status = container.querySelector('.step-viewer-status');
  const canvasHolder = container.querySelector('.step-viewer-canvas');

  button.addEventListener('click', async () => {
    button.disabled = true;
    status.hidden = false;
    status.textContent = 'Downloading and parsing STEP file (this can take a few seconds)…';

    try {
      const [occtFactory, response] = await Promise.all([loadOcctModule(), fetch(url)]);
      if (!response.ok) {
        throw new Error('Could not download the STEP file (HTTP ' + response.status + ').');
      }
      const buffer = new Uint8Array(await response.arrayBuffer());
      const result = occtFactory.ReadStepFile(buffer, null);
      if (!result.success) {
        throw new Error('The STEP parser could not read this file.');
      }

      button.remove();
      status.hidden = true;
      canvasHolder.hidden = false;
      renderModel(container, result);
    } catch (err) {
      status.textContent = 'Could not load 3D preview: ' + err.message;
      button.disabled = false;
    }
  });
}

document.querySelectorAll('.step-viewer').forEach(initStepViewer);
