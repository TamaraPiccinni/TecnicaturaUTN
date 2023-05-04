
package test;

//import ar.com.codesystem.*; //importar todos los paquetes
import ar.com.codesystem.Utileria;
//import static ar.com.codesystem.Utileria.imprimir; //solo aplica para métodos estáticos


public class TestUtileria {
    public static void main(String[] args) {
        Utileria.imprimir("Saludos a todos los alumnos de la tecnicatura"); //esta es la mejor forma
        //imprimir("Terminamos en unos minutos");
        //ar.com.codesystem.Utileria.imprimir("Ahora si estamos terminando"); //llamamos desde el paquete la clase, no es lo mas recmdable porque es mas dificil de leer
    
    }
}
