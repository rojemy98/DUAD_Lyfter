// 3. Generador de colores aleatorios con callback
// Cree una página HTML con un <div> cuadrado y un botón
// Al presionar el botón, debe:
// Generar un color aleatorio de una lista predefinida (['#FF5733', '#33FF57', '#3357FF', '#F5FF33', '#FF33F6'])
// Cambiar el color de fondo del <div>
// Mostrar el nombre del color en un <p>, mediante un callback

const colors = [
    "#FF5733",
    "#33FF57",
    "#3357FF",
    "#F5FF33",
    "#FF33F6"
];

const colorNames = [
    "Orange",
    "Green",
    "Blue",
    "Yellow",
    "Pink"
];

const box = document.getElementById("colorBox");
const button = document.getElementById("colorButton");
const paragraph = document.getElementById("colorName");


function generateColor(callback) {

    const randomIndex = Math.floor(Math.random() * colors.length);

    const color = colors[randomIndex];
    const name = colorNames[randomIndex];

    box.style.backgroundColor = color;

    callback(name);
}


function showColorName(name) {
    paragraph.textContent = `Color: ${name}`;
}


button.addEventListener("click", function() {

    generateColor(showColorName);

});