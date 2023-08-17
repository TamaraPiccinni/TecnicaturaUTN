
package ejerciocio_3;

import java.util.Scanner;

public class ejercicio_3 {
    public static void main(String[] args) {
        //rectangulo area y perimetro
        Scanner entrada = new Scanner(System.in); //clic derecho en la lampara e importo la clase scanner
        System.out.println("digite el alto del rectangulo: ");
        int alto = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el ancho del rectangulo: ");
        int ancho = Integer.parseInt(entrada.nextLine());
        int area = alto * ancho;
        int perimetro = (alto +ancho) * 2;
        System.out.println("Area = "+area);
        System.out.println("perimetro = " + perimetro);
    }
}
