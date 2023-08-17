/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se han introducido
lo hacemos primero con la clase Scanner
luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
            int numero, contador=0;
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            while(numero >=0){
                System.out.println("El numero "+numero+" es POSITIVO");
                contador++;
                System.out.println("Digite otro numero");
                numero = Integer.parseInt(entrada.nextLine());}
            System.out.println("Has introducido: "+contador+" numeros positivos");
            /* el do while no seria la mejor opcion*//*
            int numero, contador=-1;
            do{
            System.out.println("Digite un numero");
            numero = Integer.parseInt(entrada.nextLine());
            contador++;
            }while(numero >=0);
            if(numero<0);{
                System.out.println("Has introducido: "+contador+" numeros positivos");}
            System.out.println("El numero "+numero+" finaliza el programa");
        }*/
    }
}

