
// Creacion de Array o arreglos
// let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es la sintaxis vieja
const autos = ['Ferrari', 'Renault', 'BMW']; //declaramos la variable y definimos los elementos
console.log(autos); [ 'Ferrari', 'Renault', 'BMW' ]

//Recorremos los elementos de un arreglo
console.log(autos[0]); //comienzo en 0
console.log(autos[2]);

for(let i = 0;i < autos.length; i++){
    console.log(i+ ' : ' +autos[i]);
}

//Modificamos los elementos del arreglo
autos[1] = 'Volvo';
console.log(autos[1]);

//Agregar nuevos valores al arreglo
autos.push('Audi'); //Agregamos el elemento al final
console.log(autos);

//Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porch';
console.log(autos);

//Tercera forma de agregar elementos teniendo CUIDADO con la cantidad de elmentos y dejar vacio espacios
autos[6] = 'Renault'; //si coloco un numero mayor al adjudica un espacio de memoria al '5' 
console.log(autos)

//Como preguntar si es Array o Arreglo
//si uso typeof nos muestra que es tipo objet
console.log(typeof(autos)); //no usar aqui
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia
// de clase Array, booleano

console.log(typeof(autos));