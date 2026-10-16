// Cree una función que liste todos los elementos retornados de un GET al endpoint /objects,
// filtrando aquellos que no tengan data y mostrando los resultados de forma legible.

async function getObjects() {
    try {
        const response = await fetch("https://api.restful-api.dev/objects")

        if (!response.ok) {
            if (response.status === 404) {
                throw new Error("Recurso no encontrado.");
            }

            if (response.status === 401) {
                throw new Error("No autorizado para consultar recurso.");
            }

            if (response.status >= 500) {
                throw new Error("Error del servidor. Intente más tarde.");
            }

            throw new Error(`Error HTTP: ${response.status}`);
        }

        const result = await response.json();

        const filteredObjects = result.filter(
            object => object.data !== null && object.data !== undefined
        );

        console.log(filteredObjects);

        return filteredObjects;
        
    } catch (error) {
        if (error instanceof TypeError) {
            console.error("Error de red. Verifique su conexión.");
        } else {
            console.error(error.message);
        }
    }
}

getObjects()