
/*
Ejercicio1: Leer un numero y mostrar su cuadrado, repetir su proceso
hasta que se introduzca un numero negativo
JOptionPane run file muestra una ventana
*/
package Ciclos01;

import javax.swing.JOptionPane;


 class Ejercicio01{
     public static void main(String[] args) {
         int numero, cuadrado;
        /*trabaja con strin, por lo que hay que convertir.*/
         numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un nuemero: ")); 
         while(numero>=0){
             cuadrado = (int)Math.pow(numero, 2);
             System.out.println("El numero "+numero+"elevado al cuadrado el: "+cuadrado);
             numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
         }
         System.out.println("El programa a finalizado por numero negativo");
     }
}
