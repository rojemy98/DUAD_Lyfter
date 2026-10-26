// Cree una función que reciba tres parámetros: un número y dos funciones de callback.
// Si el número es par, se debe ejecutar el primer callback.
// Este debe mostrar “The number is even!”.
// Si el número es impar, se debe ejecutar el segundo.
// Este debe mostrar “The number is odd!”.

function evenNumber(){
    console.log("The number is even!")
}

function oddNumber(){
    console.log("The number is odd!")
}

function calculateEvenOrOddNumber(number, evenNumber, oddNumber) {
    if (number % 2 === 0) {
        evenNumber();
    } else {
        oddNumber();
    }
}

calculateEvenOrOddNumber(2, evenNumber, oddNumber);