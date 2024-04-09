import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setClearColor(0xffffff, 1);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
document.body.appendChild(renderer.domElement);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 1000);
camera.position.set(0, -10, 0);

// Asumiendo que has cargado tu modelo en una variable llamada `model`
const bbox = new THREE.Box3().setFromObject(model);
const center = bbox.getCenter(new THREE.Vector3());
const size = bbox.getSize(new THREE.Vector3());

// Calcular la distancia necesaria para ajustar la cámara
const maxDim = Math.max(size.x, size.y, size.z);
const fov = camera.fov * (Math.PI / 180);
let cameraZ = Math.abs(maxDim / 4 * Math.tan(fov * 2));

cameraZ *= 2; // Ajustar para dar un poco de "aire" alrededor del modelo
const cameraPosition = center.clone();
cameraPosition.z += cameraZ;

// Ajustar la cámara y los controles
camera.position.copy(cameraPosition);
controls.target.copy(center);
controls.update();
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const hotspots = [];
const mouse = new THREE.Vector2();
const raycaster = new THREE.Raycaster();

// Función para crear hotspots
function createHotspot(position, onClick) {
    const geometry = new THREE.SphereGeometry(0.05, 32, 32);
    const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const hotspot = new THREE.Mesh(geometry, material);
    hotspot.position.copy(position);
    hotspot.userData = { onClick };
    scene.add(hotspot);
    hotspots.push(hotspot);
}


// Función para cargar modelos y configurar hotspots
function loadModel(url, hotspotsConfig) {
    const loader = new GLTFLoader();
    loader.load(url, function (gltf) {
        const model = gltf.scene;
        model.traverse(function (object) {
            if (object.isMesh) {
                object.castShadow = true;
                object.receiveShadow = true;
            }
        });
        model.position.set(0, 0, -1);
        scene.add(model);
        hotspotsConfig.forEach(config => {
            createHotspot(config.position, config.onClick);
        });
        document.getElementById('progress-container').style.display = 'none';
    }, function (xhr) {
        document.getElementById('progress').innerHTML = `LOADING ${Math.round((xhr.loaded / xhr.total) * 100)}%`;
    }, function (error) {
        console.error('An error happened', error);
    });
}

renderer.domElement.addEventListener('mousedown', onDocumentMouseDown, false);

function onDocumentMouseDown(event) {
    event.preventDefault();
    
    const rect = renderer.domElement.getBoundingClientRect();
    mouse.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = - ((event.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);

    // Aquí cambiamos a intersectObjects y pasamos el array de hotspots
    const intersects = raycaster.intersectObjects(hotspots);

    // Ejecutar la acción para cada hotspot intersectado
    intersects.forEach((intersect) => {
        if (intersect.object.userData.onClick) {
            intersect.object.userData.onClick();
        }
    });
}


window.addEventListener('resize', function() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}, false);

function animate() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.render(scene, camera);
}

animate();

// Identificar la página actual y cargar el modelo y hotspots correspondientes
const currentPath = window.location.pathname;
let modelUrl;
let hotspotsConfig = [];

if (currentPath.includes('/car')) {
    modelUrl = staticModelUrl;
    hotspotsConfig = [
        // HOTSPOT CAPÓ (lateralidad, altura ,profundidad)
        { position: new THREE.Vector3(0, 0.95, 0.6), 
          onClick: function() { window.location.href = 'https://www.google.com'; }
        },
        // HOTSPOT PARACHOQUES DELANTERO
        { position: new THREE.Vector3(0, 0.55, 1.2), 
          onClick: function() { window.location.href = 'https://www.google.com'; }
        },
        // HOTSPOT PARACHOQUES TRASERO
        { position: new THREE.Vector3(0, 0.55, -3.2), 
          onClick: function() { window.location.href = 'https://www.google.com'; }
        },
        // HOTSPOT LATERAL IZQ (lateralidad, altura ,profundidad)
        { position: new THREE.Vector3(-0.85, 0.7, -1.3), 
            onClick: function() { window.location.href = 'https://www.google.com'; }
        },
        // HOTSPOT LATERAL DER
        { position: new THREE.Vector3(0.85, 0.7, -1.3), 
            onClick: function() { window.location.href = 'https://www.google.com'; }
        },
        // HOTSPOT TECHO
        { position: new THREE.Vector3(0, 1.45, -1.3), 
            onClick: function() { window.location.href = 'https://www.google.com'; }
        },        
        // ... otros hotspots para el coche ...
    ];
} else if (currentPath.includes('/moto')) {
    modelUrl = staticModelUrl;
    hotspotsConfig = [
        // Configuración de hotspots para la moto
        { position: new THREE.Vector3(2, 1, 1), onClick: () => window.location.href = 'https://www.google.com' }
        // ... otros hotspots para la moto ...
    ];
}else if (currentPath.includes('/suv')) {
    modelUrl = staticModelUrl;
    hotspotsConfig = [
        // Configuración de hotspots para la moto
        { position: new THREE.Vector3(2, 1, 1), onClick: () => window.location.href = 'https://www.google.com' }
        // ... otros hotspots para la moto ...
    ];
}

// Carga el modelo y los hotspots correspondientes.
if (modelUrl) {
    loadModel(modelUrl, hotspotsConfig);
}
