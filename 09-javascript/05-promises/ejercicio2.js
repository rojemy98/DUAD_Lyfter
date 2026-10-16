// Realice el mismo ejercicio anterior utilizando la función Promse.any() para mostrar el nombre del primer
// pokemón que esté contenido en la primera promesa que se resuelva.

const urls = [
    "https://pokeapi.co/api/v2/pokemon/1",
    "https://pokeapi.co/api/v2/pokemon/4",
    "https://pokeapi.co/api/v2/pokemon/7"
];

const promises = urls.map(url =>
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Error al obtener el Pokémon");
            }

            return response.json();
        })
);

Promise.any(promises)
    .then(pokemon => {
        console.log("Primer Pokémon recibido:", pokemon.name);
    })
    .catch(error => {
        console.error("Todas las solicitudes fallaron:", error);
    });