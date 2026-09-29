// 3. Contador de palabras en un texto
// Cree una función que cuente cuántas veces aparece cada palabra en un string
// Ignore mayúsculas/minúsculas y signos de puntuación

function countWords(text) {
    text = text.toLowerCase();
    text = text.replace(/[.,!?]/g, "");

    const words = text.split(" ");
    const wordCount = {};

    for (let i = 0; i < words.length; i++) {
        const word = words[i];

        if (wordCount[word]) {
            wordCount[word]++;
        } else {
            wordCount[word] = 1;
        }
    }

    return wordCount;
}

const text = "This is a test. This test is simple.";

console.log(countWords(text));