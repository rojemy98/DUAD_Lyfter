// Realice el mismo ejercicio anterior, pero con el URL https://reqres.in/api/users/23 para generar un error.
// Realice el manejo de error adecuado e imprima un mensaje de error indicando que el usuario no se encontró.

async function getUser() {
    try {
        const response = await fetch("https://reqres.in/api/users/23");
        if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
}

getUser();