
package Ejercicio1;
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        // Ej tienda de libros
        
        System.out.println("ingrese los siguientes datos del libro: ");
        
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("¿El envio es gratuito? (true/false)");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        System.out.println("------------------------------------------");
        System.out.println("Nombre: "+nombreLibro +"/"+ idLibro);
        System.out.println("Precio del libro es: " + precioLibro);
        System.out.println("El envio del libro es: "+envioGratuito);
        
    }
}
