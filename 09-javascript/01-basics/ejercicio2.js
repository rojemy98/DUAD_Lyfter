// Realiza un programa que recorra una lista de números y almacene todos los pares en otra lista
// Para este ejercicio intenta hacer una solución con un for y otra utilizando la función filter

const numbers = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = [];

for (let index = 0; index < numbers.length; index++) {
    if (numbers[index] % 2 === 0) {
        evenNumbers.push(numbers[index]);
    };
};
console.log(evenNumbers);


const arrayUsingFilter = numbers.filter(number => number % 2 === 0);
console.log(arrayUsingFilter);