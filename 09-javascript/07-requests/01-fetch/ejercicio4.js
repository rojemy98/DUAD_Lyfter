// Cree una función que actualice la información de un objeto, tomando
// como parámetros su ID y los nuevos datos a modificar.


async function updateObject(id, newData) {
    try {
        const response = await fetch(
            `https://api.restful-api.dev/objects/${id}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(newData)
            }
        );

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("Objeto no encontrado.");
            }

            if (response.status === 401) {
                throw new Error("No autorizado para actualizar el objeto.");
            }

            if (response.status >= 500) {
                throw new Error("Error del servidor. Intente mas tarde.");
            }

            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        console.log("Objeto actualizado correctamente:");
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

const object = {
    name: "Predator Football Boots",
    data: {
        brand: "Adidas",
        material: "Synthetic leather",
        size: "9 US",
        water_resistant: true
    }
};

updateObject("ff808181a09d98f701a14143b24c6c78", object)
