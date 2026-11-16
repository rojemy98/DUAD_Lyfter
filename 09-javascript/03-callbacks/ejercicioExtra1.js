// 1. Función con callback de validación
// Cree una función validateInput que reciba:
// Un número
// Un callback de éxito (si el número es positivo)
// Un callback de error (si el número es negativo o cero)
// Si es positivo, debe mostrar "Valid number: X"
// Si es negativo o cero, debe mostrar "Invalid number: X"

function validateInput(number, successCallback, errorCallback) {

    if (number > 0) {
        successCallback(number);
    } else {
        errorCallback(number);
    }

}

function success(number) {
    console.log(`Valid number: ${number}`);
}

function error(number) {
    console.log(`Invalid number: ${number}`);
}

validateInput(10, success, error);
validateInput(-5, success, error);
validateInput(0, success, error);