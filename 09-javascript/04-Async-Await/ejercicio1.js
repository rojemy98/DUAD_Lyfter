// Realice un programa que utilice la función fetch para solicitar un usuario del API anterior.
// El URL debe ser https://reqres.in/api/users/2. Al finalizar la solicitud, imprima los datos del usuario en pantalla.

async function getUser() {
    const response = await fetch("https://reqres.in/api/users/2");
    const result = await response.json();
    console.log(result);
}

getUser();

