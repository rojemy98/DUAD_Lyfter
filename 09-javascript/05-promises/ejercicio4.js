// Repita los ejercicios 1 y 2 de la sección de Async/Await resolviéndolos con las funciones .then(), .catch() y .finally()
// de ser requerido.


// =====================================
// Ejercicio 1: Promise.all()
// =====================================

const urlsAll = [
    "https://pokeapi.co/api/v2/pokemon/1",
    "https://pokeapi.co/api/v2/pokemon/2",
    "https://pokeapi.co/api/v2/pokemon/3"
];

const promisesAll = urlsAll.map(url =>
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            return response.json();
        })
);

Promise.all(promisesAll)
    .then(pokemonListAll => {
        console.log("\n--- Ejercicio 1: Promise.all() ---");

        pokemonListAll.forEach(pokemon => {
            console.log(pokemon.name);
        });
    })
    .catch(error => {
        console.error("Error en Promise.all():", error.message);
    })
    .finally(() => {
        console.log("Proceso Promise.all() finalizado.");
    });


// =====================================
// Ejercicio 2: Promise.any()
// =====================================

const urlsAny = [
    "https://pokeapi.co/api/v2/pokemon/1",
    "https://pokeapi.co/api/v2/pokemon/4",
    "https://pokeapi.co/api/v2/pokemon/7"
];

const promisesAny = urlsAny.map(url =>
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            return response.json();
        })
);

Promise.any(promisesAny)
    .then(firstPokemon => {
        console.log("\n--- Ejercicio 2: Promise.any() ---");
        console.log("Primer Pokémon recibido:", firstPokemon.name);
    })
    .catch(error => {
        console.error("Error en Promise.any():", error.message);
    })
    .finally(() => {
        console.log("Proceso Promise.any() finalizado.");
    });