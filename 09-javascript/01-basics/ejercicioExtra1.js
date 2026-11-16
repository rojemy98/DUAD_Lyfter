// 1. Revertir un string sin usar .reverse()
// Cree una función que reciba un string y devuelva el string al revés sin usar split(), reverse(), ni join()
// Deberá recorrerlo con un for

// Ejemplo:

// Entrada:
// "JavaScript"

// Salida:
// "tpircSavaJ"


function reversedString(word) {  

    let reversedWord = ""

    for (let index = word.length - 1; index >= 0; index--) {
        const letter = word[index];
        reversedWord = reversedWord + letter;
    }

    return reversedWord;
}

console.log(reversedString("JavaScript"));
