
import java.util.Scanner;

/*
Estructura if else
Determinar si un alumno aprueba o reprueba un curso, sabiendo que
aprobara si su promedio de tres calificaciones es mayor o igual a 70
reprueba caso contrario
*/
public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); //para poder pedir los valores al usuario
        float nota1,nota2,nota3,promedio;
        System.out.println("Digite la 1º calificacion");
        nota1 = entrada.nextFloat();
        System.out.println("Digite la 2º calificacion");
        nota2 = entrada.nextFloat();
        System.out.println("Digite la 3º calificacion");
        nota3 = entrada.nextFloat();
        promedio= (nota1+nota2+nota3)/3;
        if (promedio>= 70){
            System.out.println("Aprobo con: "+promedio+" de promedio");
        }else{
            System.out.println("Reprobo con: "+promedio+" de promedio");
    }
}
}
