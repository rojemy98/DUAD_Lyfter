// Cree cuatro promesas, donde cada una resuelve a una de las palabras de la lista ["very", "dogs", "cute", "are"] respectivamente, 
// en el mismo orden. Utilice la combinación de la función setTimeout y Promse.all() para obtener la salida "Dogs are very cute" ,
// sin modificar el orden de la lista manualmente o mediante un sort.

const words = ["very", "dogs", "cute", "are"];

const completedWords = [];

const promises = words.map((word, index) => {
    // El tiempo depende de la posicion, no de la palabra.
    const delay = index % 2 === 0
        ? (index / 2 + 3) * 1000
        : ((index + 1) / 2) * 1000;

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