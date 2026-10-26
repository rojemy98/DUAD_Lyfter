// Cree dos archivos de texto con el siguiente contenido.
// Lea ambos archivos y compare cuales palabras se repiten en ambos. Muestre el mensaje escondido al final del programa.

const fs = require("fs");

function readFile(fileName, callback) {
    fs.readFile(fileName, "utf-8", (error, data) => {
        if (error) {
            console.log("Error reading file:", error);
            return;
        }

        callback(data);
    });
}

readFile("09-javascript/03-callbacks/file1.txt", (data1) => {

    readFile("09-javascript/03-callbacks/file2.txt", (data2) => {

        const words1 = data1.split("\n").map(word => word.trim());
        const words2 = data2.split("\n").map(word => word.trim());

        const repeatedWords = words1.filter(word => words2.includes(word));

        console.log(repeatedWords.join(" "));
    });

});