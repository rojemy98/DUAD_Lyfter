// Cree una función que liste todos los elementos retornados de un GET al endpoint /objects,
// filtrando aquellos que no tengan data y mostrando los resultados de forma legible.

const axios = require("axios");

async function getObjects() {
    try {
        const response = await axios.get(
            "https://api.restful-api.dev/objects"
        );

        const filteredObjects = response.data.filter(
            object => object.data !== null && object.data !== undefined
        );

        console.table(filteredObjects);

        return filteredObjects;

    } catch (error) {
        if (error.response) {
            if (error.response.status === 404) {
                console.error("Recurso no encontrado.");
            } else if (error.response.status === 401) {
                console.error("No autorizado para consultar el recurso.");
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
    }
}

getObjects();
