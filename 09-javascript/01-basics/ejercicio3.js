// Toma una lista de temperaturas en grados celsius y conviertala a farenheit utilizando la función map

const celsius = [-10, 0, 5, 10];

const farenheit = celsius.map( celsius => (celsius * 9/5) + 32 )

console.log(farenheit) 