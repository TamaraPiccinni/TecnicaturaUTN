
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
    //creamos un objeto llamado aritmetica1 que trabaja en el espacio de memoria del constructor
    //Aritmetica() llamamos a la clase =al constructor y reserva espacio de memoria
        var a = 10; //variables locales
        int b = 7; //Memoria stack
        miMetodo(); //Llamamos el método 
        Aritmetica aritmetica1 = new Aritmetica(); //con new llamo al constructor esto lo asigna al objeto
        aritmetica1.a = 3; //aca modifico el valor de los atrubitos por medio del . 
        aritmetica1.b = 7; // objeto aritmetica1 usando el operador de . "punto"
        aritmetica1.sumarNumeros();
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        //pruebo el metodo con sumar con retorno
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
    
        //vamos a llamar a travez del objeto con el operador de punto al metodo sumarConRetorno
        //damos 2 argumentos del tipo entero
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
        
        System.out.println("aritmetica1 a: "+aritmetica1.a);
        System.out.println("aritmetica1 b: "+aritmetica1.b);
        
          Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no de debe hacer lo hace solo
        //System.gc(); método para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud"); //creamos un objeto de tipo string (persona) desde la clase de abajo persona, le paso los argumentos
                //o hace falta aclara que es string (new string....) asi lo asigno en memoria hip no con stack
                // aui se utiliza un tipo de memoria pullstraun (es mas eficiente)
                System.out.println("persona = " + persona);
                System.out.println("Persona nombre : "+persona.nombre);
                System.out.println("Persona apellido : "+persona.apellido);
    }
    //aqui puedo creaer otro metedo
    //Modularidad creamos un nuevo método
    public static void miMetodo(){
        //a = 10; //una variable esta limitada
        System.out.println("Aquí hay otro método");
    }

}
//Creamos una nueva clase solo puede haber una clase publica
// x dafaull el modificador de acceso es defaull o package pero no se escribe como public
//esta clase solo se puede acceder desde la otra clase defindas desde el mismo paquete 
//aqui es packege operaciones
class Persona{
    String nombre; //atributos
    String apellido; //atributo
    //metodo sin asignar modificador de acceso, ya es default.. metodo constructor
    Persona(String nombre, String apellido){ //Constructor
        super(); //este es el constructor vacio de la clase Padre objet
        //todas las clases tienen herencia de la clase objet
        //Imprimir imprimir = new Imprimir(); //forma que veniamos creando un objeto
        //nueva forma de crear un objeto
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Obejeto pesona usando this: "+this); //con this imprimimos el objeot
    }
}
//otra nueva clase
class Imprimir{
    public Imprimir(){ //metodo constructor
        super(); //constructo de la clase padre, para reservar memoria
    }
    //otro metedo mas que no va a regresar nada
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresión del objeto actual (this): "+this);
    }
}