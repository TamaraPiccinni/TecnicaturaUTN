
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osavaldo", 57.001, false);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        //Modificamos a través de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre ="Juan Ignacio"; //Da error xq ya no se puede utilizar
        //System.out.println("Nombre es: = " + persona1.nombre); //Tambien es error
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo:" +persona1.getSueldo() );
        System.out.println("persona1 para obtener el booleano " + persona1.isEliminado() );
        //Tarea: Crear otro objeto de tipo Perosna. asigna valores de manera inicial
        //e imprimir, luego modificar sus valotes y volver a imprimir
        
    }
}
