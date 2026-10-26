// Cree una función que tome como parámetro la información de un objeto y cree un nuevo objeto utilizando el
// endpoint POST. Piense en al menos 4 o 5 atributos que debería tener un artículo deportivo (usted decide cuáles)
// y envíelos dentro de data.

async function createObject(newObject) {
    try {
        const response = await fetch(
            "https://api.restful-api.dev/objects",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(newObject)
            }
        );

        if (!response.ok) {
            if (response.status === 400) {
                throw new Error("Datos inválidos. Verifique la información del objeto.");
            }

            if (response.status === 401) {
                throw new Error("No autorizado para crear el objeto.");
            }

            if (response.status === 403) {
                throw new Error("No tiene permisos para crear el objeto.");
            }

            if (response.status >= 500) {
                throw new Error("Error del servidor. Intente más tarde.");
            }

            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();
        
        console.log("Object created successfully:");
        console.log(result);

        return result;

    } catch (error) {
        if (error instanceof TypeError) {
            console.error("Error de red. Verifique su conexión.");
        } else {
            console.error("Error:", error.message);
        }

        throw error;
    }
}

const object = {
    "name": "Air Zoom Running Shoes",
    "data":{
        "brand": "Nike",
        "material": "Breathable mesh and rubber",
        "size": "10.5 US",
        "water_resistant": true
    }
}

createObject(object);