
package Ejercicio2;
import java.util.Scanner;
public class Ejercicio2 {
    public static void main(String[] args) { //psvm + tab
        //hacer un programa que calcule el salario a partir de sus horas y de su salario por hora
        Scanner entrada = new Scanner(System.in);
        int horasSemanales;
        float salarioHora, salarioTotal;
        System.out.println("Digite la cantidad de horas trabajadas");
        horasSemanales = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el pago por hora: ");
        salarioHora = Float.parseFloat(entrada.nextLine());
        salarioTotal = horasSemanales * salarioHora;
        System.out.println("\nsalarioTotal: US$" + salarioTotal);
        
    }
    
}
