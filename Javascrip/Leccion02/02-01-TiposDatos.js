//Tipos de datos en JAvaScrip
/* comentario para multiples comentarios
igual a java
*/

var nombre = 'Ariel'; //Tipo String
console.log(nombre);

var numero = 3000; // Tipo Numérico
console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"
}

console.log(objeto);
//(typeof muestra el tipo, no hace fata definir el tipo)
//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion 
function miFuncion(){}
console.log(typeof miFuncion); 

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato undefined (por defaull)
var x;
console.log(typeof x);

x = undefined; //aqui se lo asigno
console.log(typeof x);

// null: significa ausencia de valor (una variable sin asignacion vacia)
var y  = null; //null no es un tipo de dato pero su origen es de tipo objet
console.log(typeof y);

//Tipo de dato de array y Empy String (son de tipo objet, distinto a otros lenguajes)
var autos = ['Citroen', 'Audi', ' BMW', 'Ford']; //en te [] es un arreglo
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z); //esto se refiere a una cadena vacia:
console.log(typeof z);