var nombre = "Jose";
var apellido = " Montes";
var nombreCompleto = nombre+' '+apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud';
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo nuemro como str
console.log(juntos);
juntos = nombre +78 +17; //aqui puedo diferenciar con parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //(tercera concatenacion) Concatenamos usando el operador simplificado
console.log(nombre);

//hoy en ves de var usaremos let y cosnt
Let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; una constante no puede ser modificada
console.log(apellido2); //console es un obeto que llama al metodo (o funcion que es lo mismo) los y le pasamos argumentos

let x, y; // se pueden crear varias variebles dentro de una misma linea
x = 17,y = 21; //se puede hacer la asignacion de varias variables dentro de la misma liena
let z = = x +y; //se asigna el valor de la operacion
console.log(z);

let _1num =331; //No utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe"; //No utlizas palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);
