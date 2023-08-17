
package Clases;

public class PruebaPersona {//PasclaCase
    //desde este metodo main podemos crear otros objetos
    public static void main(String[] args) {
        Persona persona1;// creo una variable tipo persona
        persona1 = new Persona(); // Llamamos al consructor 
        //(tranforamamos a la variable en objeto.. la instanciamos
        //la variable persona1 al asociarla al contructor pasa a ser un objeto
        //el constructor almacena en otra parte (reserva espacio)
        persona1.nombre = "Tamara"; //Tamara es una caracteristica
        persona1.apellido = "Piccinni";//EL valor hexadecimal normalmente comienza 0x
        persona1.obtenerInformacion(); //llamo al metodo y muestra los valores
        
        //instancear = crear un objeto
        //creamos un nuevo objeto (lo hacemos en una sola linea)
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); // al no asiganarle un valor
        System.out.println("persona1 = " + persona1);
        //nos muestra el lugar conde se almaceno
        persona2.obtenerInformacion(); //muestra la info aunque no tenga nungun valor
        persona2.nombre = "Ariel";
        persona2.apellido = "Betancud";
        persona2.obtenerInformacion(); // ahora muestra los valores
        
    }
}
