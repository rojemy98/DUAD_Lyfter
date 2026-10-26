// Cree una función que actualice la información de un objeto, tomando
// como parámetros su ID y los nuevos datos a modificar.


const axios = require("axios");

async function updateObject(id, newData) {
    try {
        const response = await axios.put(
            `https://api.restful-api.dev/objects/${id}`,
            newData
        );

        console.log("Objeto actualizado correctamente:");
        console.log(response.data);

        return response.data;

    } catch (error) {
        if (error.response) {
            if (error.response.status === 404) {
                console.error("Objeto no encontrado.");
            } else if (error.response.status === 401) {
                console.error("No autorizado para actualizar el objeto.");
            } else if (error.response.status >= 500) {
                console.error("Error del servidor. Intente más tarde.");
            } else {
                console.error(`Error HTTP: ${error.response.status}`);
            }
        } else if (error.request) {
            console.error("No se recibió respuesta del servidor.");
        } else {
            console.error("Error:", error.message);
        }

        return null;
    }
}

const object = {
    name: "Pro Basketball",
    data: {
        brand: "Spalding",
        material: "Composite leather",
        size: "Size 7",
        water_resistant: true
    }
};

updateObject("ff808181a09d98f701a14143b24c6c78", object);
