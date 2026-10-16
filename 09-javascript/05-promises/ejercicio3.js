// Cree cuatro promesas, donde cada una resuelve a una de las palabras de la lista ["very", "dogs", "cute", "are"] respectivamente, 
// en el mismo orden. Utilice la combinación de la función setTimeout y Promse.all() para obtener la salida "Dogs are very cute" ,
// sin modificar el orden de la lista manualmente o mediante un sort.

const words = ["very", "dogs", "cute", "are"];

// Tiempo de espera en segundos para cada posicion:
// very: 3 s, dogs: 1 s, cute: 4 s, are: 2 s.
const delays = [3, 1, 4, 2];

const completedWords = [];

const promises = words.map((word, index) => {
    const delay = delays[index] * 1000;

    return new Promise(resolve => {
        setTimeout(() => {
            completedWords.push(word);
            console.log(`Palabra recibida: ${word}`);

            resolve(word);
        }, delay);
    });
});

Promise.all(promises)
    .then(() => {
        const sentence = completedWords.join(" ");

        console.log(
            sentence.charAt(0).toUpperCase() + sentence.slice(1)
        );
    })
    .catch(error => {
        console.error("Error:", error);
    });