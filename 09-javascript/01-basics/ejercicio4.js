// Toma un string y conviertelo en una lista de palabras, separandolas por espacios en blanco. No puedes usar la función split.

const example = "This is a string!";

const result = [];
let word = "";

for (let index = 0; index < example.length; index++) {

    const letter = example[index];

    if (letter !== " ") {
        word += letter;
    } else {
        result.push(word);
        word = "";
    }
}

result.push(word);

console.log(result);