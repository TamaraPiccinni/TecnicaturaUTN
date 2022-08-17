
package Leccion_2;

import java.util.Scanner;

public class Leccion_2 {
    public static void main(String[] args) {
//        var condicion = true;
//        if(condicion){ //la variable es de tipo booleana no hace falta poner == true
//            System.out.println("Condicion Verdadera"); //condicional simple
//        }
//        else{
//            System.out.println("Condicion Falsa"); //condicion doble
//        }
//        var numero = 2; //codigo duro
//        var numeroTexto = "Numero desconocido"; //iniciamos, creamos una cadena
//        if(numero == 1){ //inferendia de tipos es string
//            numeroTexto = "Numero uno"; 
//        }
//        else if(numero == 2){
//            numeroTexto = "Numero dos";
//        }
//        else if(numero == 3){
//            numeroTexto = "Numero tres";
//        }
//        else if(numero == 4){
//            numeroTexto = "Numero cuatro";
//        }
//        else{
//            numeroTexto = "Numero no encontrado";
//        }
//        System.out.println("numeroTexto = " + numeroTexto);

//switch no es booleano es numerico o string
//hace falta un break para salir y que no se pise
Scanner entrada = new Scanner(System.in); //para poder pedir los valores al usuario
        System.out.println("Digite un numero del 1 al 4: ");
var numero = Integer.parseInt(entrada.nextLine()); 
var numeroTexto = "Valor desconocido";
switch(numero){
    case 1:
        numeroTexto = "numero uno";
        break;
    case 2:
        numeroTexto = "numero dos";
        break;
    case 3:
        numeroTexto = "numero tres";
        break;
    case 4:
        numeroTexto = "numero cuatro";
        break;
    default:
        numeroTexto = "numero no encontrado";
        
}
System.out.println("numeroTexto = " + numeroTexto);
    }
}
