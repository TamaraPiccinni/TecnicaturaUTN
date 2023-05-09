// while (mientras)
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//do while (primero se ejecuta el ciclo y luego revisa la condicion)

let conteo =0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log("Fin del ciclo do while");

//for 
for(let contando = 0; contando < 3; contando++ ){
    console.log(contando); 0, 1, 2
}
console.log("Fin del ciclo for");

// Palabra reservada Break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando); //Muestra solo los pares
        break; //solo muestra el primer
    }
}
console.log("Termina el ciclo al encontrar el primer número par");

// Palabra reservada continue y Etiquetas Labels (estas etiquetas no son recomendadas)
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 != 0){
        break inicio; //va a ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo");

