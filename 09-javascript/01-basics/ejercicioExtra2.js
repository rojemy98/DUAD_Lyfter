// 2. Eliminar números duplicados de una lista
// Cree una función que reciba una lista de números y devuelva una nueva
// lista sin números repetidos, manteniendo el orden original


function uniqueNumbers(listNumbers){

    const uniqueNumbers = [];

    for (let i = 0; i < listNumbers.length; i++) {
        const number = listNumbers[i];

        let exists = false;

        for (let j = 0; j < uniqueNumbers.length; j++) {
            if (number === uniqueNumbers[j]) {
                exists = true;
            }
        }

        if (!exists) {
            uniqueNumbers.push(number);
        }
    }

    return uniqueNumbers
}

console.log(uniqueNumbers([1, 2, 3, 2, 4, 1, 5]))