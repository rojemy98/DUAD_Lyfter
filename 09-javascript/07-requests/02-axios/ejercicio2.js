// Cree una función que tome como parámetro la información de un objeto y cree un nuevo objeto utilizando el
// endpoint POST. Piense en al menos 4 o 5 atributos que debería tener un artículo deportivo (usted decide cuáles)
// y envíelos dentro de data.


const axios = require("axios");

async function createObject(newData) {
    try {
        const response = await axios.post(
            "https://api.restful-api.dev/objects",
            newData
        );

        console.log("Objeto creado correctamente:");
        console.log(response.data);

        return response.data;

    } catch (error) {
        if (error.response) {
            if (error.response.status === 400) {
                console.error("Los datos enviados son inválidos.");
            } else if (error.response.status === 401) {
                console.error("No autorizado para crear el objeto.");
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
    name: "Pro Tennis Racket",
    data: {
        brand: "Wilson",
        material: "Graphite",
        size: "27 inches",
        water_resistant: false
    }
};

createObject(object);
