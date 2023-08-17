
package ejercicio_4;

import java.util.Scanner;

public class ejercicio_4 {
    public static void main(String[] args) { //psvm +tab para creal el main
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un numero ");
        int num1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Digite otro numero ");
        int num2 = Integer.parseInt(entrada.nextLine());
        System.out.print("El numero mayor es = ");
        System.out.print(num1 > num2 ? num1 : num2 );
        System.out.println("");
    }
}
