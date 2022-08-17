
import java.util.Scanner;

/*
Clase 11
Ejercicio 2
En un almacen se hacen 20 % de descuento a los clientes cuando supera los $100 
¿Cual sera la cantidad que pagara una persona por su compra?
*/
public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in); //para poder peir los valores al usuario
        float compra,precioFinal;
        System.out.println("Digite la cantidad a pagar");
        compra = Float.parseFloat(entrada.nextLine());
        if (compra>100){
            precioFinal = (float) (compra*0.8);
            
        }else{
            precioFinal= compra;
    }
     System.out.println("El precio a pagar es: $" + precioFinal);
                
    }
}
