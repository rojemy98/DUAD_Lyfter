// Realice un programa que utilice la función fetch para solicitar un usuario del API anterior.
// El URL debe ser https://reqres.in/api/users/2. Al finalizar la solicitud, imprima los datos del usuario en pantalla.

async function getUser() {
    try {
        const response = await fetch("https://reqres.in/api/users/2");

        if (!response.ok) {
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        console.log(result.data);

    } catch (error) {
        console.error("Error al obtener el usuario:", error.message);
    }
}

getUser();