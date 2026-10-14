// 2. Simulación de carga concurrente y secuencial
// Cree una función que simule la carga de diferentes recursos (imágenes, scripts, estilos) usando setTimeout y devuelva una Promise
// Simule:
// Cargar imágenes en paralelo (Promise.all)
// Cargar scripts uno después del otro
// Mostrar un mensaje cuando todo el sitio esté cargado

// Función que simula la carga de un recurso
function loadResource(type, name, time) {
    return new Promise((resolve) => {
        console.log(`Cargando ${type}: ${name}...`);

        setTimeout(() => {
            console.log(`${type} cargado: ${name}`);
            resolve(name);
        }, time);
    });
}

// Cargar imágenes en paralelo
const loadImages = () => {
    return Promise.all([
        loadResource("Imagen", "logo.png", 2000),
        loadResource("Imagen", "banner.jpg", 3000),
        loadResource("Imagen", "background.png", 1500)
    ]);
};

// Cargar scripts secuencialmente
const loadScripts = () => {
    return loadResource("Script", "library.js", 2000)
        .then(() => loadResource("Script", "app.js", 1500))
        .then(() => loadResource("Script", "analytics.js", 1000));
};

// Cargar todos los recursos del sitio
console.log("Iniciando carga del sitio...\n");

Promise.all([
    loadImages(),
    loadScripts(),
    loadResource("Estilo", "styles.css", 2500)
])
    .then(() => {
        console.log("\nTodo el sitio está cargado");
    })
    .catch(error => {
        console.error("Error al cargar el sitio:", error);
    });