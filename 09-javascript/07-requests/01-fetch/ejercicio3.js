// Cree una función que retorne un objeto del API, tomando su ID como parámetro.

async function getObject(id) {

    try {
        const response = await fetch(`https://api.restful-api.dev/objects/${id}`)

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("Articulo no encontrado.");
            }

            if (response.status === 401) {
                throw new Error("No autorizado para consultar el articulo.");
            }

            if (response.status >= 500) {
                throw new Error("Error del servidor. Intente más tarde.");
            }

            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        console.log(result);

        return result;
        
    } catch (error) {
        if (error instanceof TypeError) {
            console.error("Error de red. Verifique su conexión.");
        } else {
            console.error(error.message);
        }

    return null;
    }
}

getObject("ff808181a09d98f701a14143b24c6c78")
