// Cree una función que retorne un objeto del API, tomando su ID como parámetro.

const axios = require("axios");

async function getObject(id) {
    try {
        const response = await axios.get(`https://api.restful-api.dev/objects${id}`);

        console.log(response.data);

        return response.data;

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

        return null;
    }
}

