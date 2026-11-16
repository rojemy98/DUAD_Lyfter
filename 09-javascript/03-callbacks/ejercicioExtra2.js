// 2. Leer listas de nombres y encontrar coincidencias
// Cree dos arrays de strings simulando nombres de personas
// Cree una función que:
// Reciba los dos arrays y un callback
// El callback se encargue de mostrar en consola todos los nombres que aparecen en ambas listas
// No use funciones prehechas como filter, hágalos con for y callbacks

const names1 = ["John", "Mary", "Peter", "Anna", "David"];
const names2 = ["Luis", "Anna", "David", "Sarah", "Peter"];

function findMatches(array1, array2, callback) {

    const matches = [];

    for (let i = 0; i < array1.length; i++) {

        for (let j = 0; j < array2.length; j++) {

            if (array1[i] === array2[j]) {
                matches.push(array1[i]);
            }

        }

    }

    callback(matches);
}

function showMatches(matches) {

    console.log("Names found in both lists:");

    for (let i = 0; i < matches.length; i++) {
        console.log(matches[i]);
    }

}

findMatches(names1, names2, showMatches);