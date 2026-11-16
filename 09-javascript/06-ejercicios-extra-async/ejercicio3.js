// 3. Temporizador con Promesa
// Cree una función wait(seconds) que:
// Reciba una cantidad de segundos y devuelva una Promise
// Cuando se cumpla el tiempo, imprima "Han pasado X segundos"
// Llame a esta función 3 veces:
// Primero 2 segundos
// Luego 3 segundos
// Finalmente 1 segundo
// El mensaje debe imprimirse solo después que cada tiempo individual se cumpla (no en paralelo)

function wait(seconds) {
    return new Promise(resolve => {
        setTimeout(() => {
            console.log(`Han pasado ${seconds} segundos`);
            resolve();
        }, seconds * 1000);
    });
}

wait(2)
    .then(() => wait(3))
    .then(() => wait(1));