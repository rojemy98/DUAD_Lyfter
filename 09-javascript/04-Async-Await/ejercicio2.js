// Realice el mismo ejercicio anterior, pero con el URL https://reqres.in/api/users/23 para generar un error.
// Realice el manejo de error adecuado e imprima un mensaje de error indicando que el usuario no se encontró.

async function getUser() {
    try {
        const response = await fetch("https://reqres.in/api/users/23");

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

        console.log(result.data);

    } catch (error) {
        if (error instanceof TypeError) {
            console.error("Error de red. Verifique su conexión.");
        } else {
            console.error(error.message);
        }
    }
}

getUser();