// Cree una función que retorne un objeto del API, tomando su ID como parámetro.

async function getObject(id) {

    try {
        const response = await fetch(`https://api.restful-api.dev/objects/${id}`)

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("Usuario no encontrado.");
            }

            if (response.status === 401) {
                throw new Error("No autorizado para consultar el usuario.");
            }

            if (response.status >= 500) {
                throw new Error("Error del servidor. Intente más tarde.");
            }

            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        console.log(result);
        
    } catch (error) {
        if (error instanceof TypeError) {
            console.error("Error de red. Verifique su conexión.");
        } else {
            console.error(error.message);
        }
    }
}

getObject("ff808181a09d98f701a14143b24c6c78")
