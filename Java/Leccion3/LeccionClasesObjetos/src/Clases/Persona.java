/*una clase es una plantilla donde vamos a trabajar
* Tiene un nombre
* Tiene atributos y metodos*/
/* Un objeto es una intancia de una clase*/
/*se usa pascalCase*/
//carcateristicas = "Atributos"
//Acciones = "Metodos"
//una clase es un nuevo tipo definido
//podemos usar el metodo main (se recomienda hacerlo fuera de la clase)
package Clases;

public class Persona {
    //Atributos de la clase (caracteristicas que se asocian a una clase)
    String nombre;
    String apellido;
    
    //Metodos de la clase (acciones, una parte que puedo reutilizar)
    // Recibe valores = "Argumentos"
    // Retornar un valor = "Valor de retorno" (ese valor tambien puede retornar al metodo)
    // creamos un  metodo
    //public inica que se puede usar fuera de esta clase (es el modificador de acceso)
    //void indica que no regresa ningun tipo de informacion
    //usamos CamelCase en el nombre
    // los parentesis indicar que podemos recibir informacion (esta se conoce como argumento)
    
    public void obtenerInformacion() { //asi definimos el metodo dentro de la clase
        //para imprimir los atributos de la clase
        System.out.println("Nombre"+nombre); //concatenamos el atrubito nombre (no es una simple valiable
        //es un atributo de la clase,. aunque no este definido dentro del metodo 
        //al ser un atributo se puede usar dentro de cualquier metodo
        System.out.println("apellido"+apellido);
        
        //como crear un objeto partendo de la clase persona
        //una clase es nuestra plantilla
        //Aun no sabemos el nombre y el apellido ya que no establecimos los valores de los atributos
        //crear 2 objetos que les vamos a poner nombre y apellido a cada uno
    }  
}
// ctrl + 7 despliega el Navegador (pestaña de Windows)