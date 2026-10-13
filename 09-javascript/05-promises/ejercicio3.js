// Cree cuatro promesas, donde cada una resuelve a una de las palabras de la lista ["very", "dogs", "cute", "are"] respectivamente, 
// en el mismo orden. Utilice la combinación de la función setTimeout y Promse.all() para obtener la salida "Dogs are very cute" ,
// sin modificar el orden de la lista manualmente o mediante un sort.

const words = ["very", "dogs", "cute", "are"];

const promises = words.map(word => {
    return new Promise(resolve => {
        let delay;

        switch (word) {
            case "dogs":
                delay = 1000;
                break;
            case "are":
                delay = 2000;
                break;
            case "very":
                delay = 3000;
                break;
            case "cute":
                delay = 4000;
                break;
        }

        setTimeout(() => {
            resolve(word);
        }, delay);
    });
});

Promise.all(promises)
    .then(results => {
        console.log(
            results[1].charAt(0).toUpperCase() +
            results[1].slice(1) + " " +
            results[3] + " " +
            results[0] + " " +
            results[2]
        );
    });