// Repita los ejercicios 1 y 2 de la sección de Async/Await resolviéndolos con las funciones .then(), .catch() y .finally()
// de ser requerido.

function getUser() {
    fetch("https://reqres.in/api/users/2")
        .then(response => response.json())
        .then(result => {
            console.log(result);
        })
        .catch(error => {
            console.error("Error:", error.message);
        })
        .finally(() => {
            console.log("Solicitud finalizada.");
        });
}

getUser();

function getUserError() {
    fetch("https://reqres.in/api/users/23")
        .then(response => {
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }

            return response.json();
        })
        .then(result => {
            console.log(result);
        })
        .catch(error => {
            console.error(error.message);
        })
        .finally(() => {
            console.log("Solicitud finalizada.");
        });
}

getUserError();