// Utilice el API https://pokeapi.co/api/v2/pokemon/:ID para solicitar 3 distintos pokemónes.
// Utilice la función Promise.all() para mostrar en pantalla el nombre de los tres pokemónes al mismo tiempo,
// hasta que todas las promesas se resuelvan.

const urls = [
    "https://pokeapi.co/api/v2/pokemon/1",
    "https://pokeapi.co/api/v2/pokemon/2",
    "https://pokeapi.co/api/v2/pokemon/3"
];

const promises = urls.map(url => fetch(url));

Promise.all(promises)
    .then(responses => {
        responses.forEach(response => {
            if (!response.ok) {
                throw new Error("Error al obtener los Pokémon");
            }
        });

        return Promise.all(
            responses.map(response => response.json())
        );
    })
    .then(pokemonList => {
        pokemonList.forEach(pokemon => {
            console.log(pokemon.name);
        });
    })
    .catch(error => {
        console.error("Ocurrió un error:", error.message);
    });