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
            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        console.log("Objet created successfully:");
        console.log(result);

    } catch (error) {
        console.error("Error:", error.message);
    }
}

object = {
    "name": "Air Zoom Running Shoes",
    "data":{
        "brand": "Nike",
        "material": "Breathable mesh and rubber",
        "size": "10.5 US",
        "water_resistant": true
    }
}

createObject(object);