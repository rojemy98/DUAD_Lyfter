// Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los siguientes datos:

// Entrada
const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
}

// Salida:
// Nombre del estudiante,
// Promedio de notas
// Materia con la nota más alta
// Materia con la nota más baja

let total = 0;
let highestGrade = student.grades[0];
let lowestGrade = student.grades[0];

for (let index = 0; index < student.grades.length; index++) {

    const currentGrade = student.grades[index];

    total += currentGrade.grade;

    if (currentGrade.grade > highestGrade.grade) {
        highestGrade = currentGrade;
    }

    if (currentGrade.grade < lowestGrade.grade) {
        lowestGrade = currentGrade;
    }
}

const result = {
    name: student.name,
    gradeAvg: total / student.grades.length,
    highesGrade: highestGrade.name,
    lowestGrade: lowestGrade.name
};

console.log(result);