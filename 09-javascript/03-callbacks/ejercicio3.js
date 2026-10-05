// Cree una pequeña página web con un botón y un <p> donde al presionar el botón,
// cambia el color del fondo del <p> por uno aleatorio de la siguiente lista
// [red, blue, green, yellow, cyan, pink]. Para el texto puede utilzar un
// Lorem Ipsum corto, solamente para rellenar el espacio. La acción del botón debe
// agregarla con un listener

const colors = ["red", "blue", "green", "yellow", "cyan", "pink"];

const paragraph = document.getElementById("text");
const button = document.getElementById("colorButton");

button.addEventListener("click", () => {

    const randomIndex = Math.floor(Math.random() * colors.length);

    paragraph.style.backgroundColor = colors[randomIndex];

});