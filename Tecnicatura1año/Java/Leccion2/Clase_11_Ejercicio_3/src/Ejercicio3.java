
import java.util.Scanner;

/*
Clase 11
Ejercicio 3
Leer 2 numeros. si son iguales que los multiplique
si el primeo es mayor que el segundo que los reste
sino que los sume
*/
public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float num1,num2,resultado;
        System.out.println("Digite el primer numero: ");
        num1=Float.parseFloat(entrada.nextLine());
        System.out.println("Digite el segundo numero: ");
        num2=Float.parseFloat(entrada.nextLine());
        if (num1==num2){
            resultado =num1*num2;
        }else if(num1>num2){
            resultado=num1-num2;
        }else{
            resultado=num1+num2;
        }
        System.out.println("El resultado es: "+resultado);
    }
}
