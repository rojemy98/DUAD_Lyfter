// 1. Peticiones encadenadas (secuenciales)
// Utilizando el API de ReqRes (https://reqres.in/api/users/), realice lo siguiente:
// Solicite el usuario 2
// Cuando termine, solicite el usuario 3
// Cuando termine, solicite el usuario 4
// Cada usuario debe imprimirse solo cuando la petición anterior haya finalizado correctamente
// Si alguna petición falla, debe detener el flujo y mostrar un mensaje de error
// Puede resolver con async/await o .then() según prefiera

function getUser(id) {
    return fetch(`https://reqres.in/api/users/${id}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error al obtener el usuario ${id}: ${response.status}`);
            }

            return response.json();
        })
        .then(data => {
            console.log(data);
            return data;
        });
}

getUser(2)
    .then(() => getUser(3))
    .then(() => getUser(4))
    .catch(error => {
        console.error("La secuencia se detuvo:", error.message);
    });