/* Atributos y metodos empiezan con minuscula (camelCase
clase se empeiza con mayuscula PascalCase)
*/
package Operaciones;

public class Aritmetica {
    public static void main(String[] args) {
    }
    //Atributos de la clase
    int a; //por default es 0 (al no inicializarla int es 0, bolleano es false) 
    int b; //no estan vacias, tienen el valor default
    
    /*El constructor es un método especial
    El constructor cumple 3 objetivos
    1 contruye un objeto
    2.Reserva un espacio de memoria
    3. Inicializa los trubutos de la clase
    si voy a hacer el segundo y necesito el primero x defecto debo crearlo antes*/
    //Primer ejemplo es el que crea x defecto java x defecto omitiendo valores
    public Aritmetica(){ //Constructor 1 vacio
        System.out.println("Se esta ejecutando este constructor número uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores asignando valores
    public Aritmetica(int a, int b){ //Constructor 2 
        //(la diferencia con el primero es que en este le agrego parametos que inicializan los atributos)
        //los parametros que ingresamos no pueden ser del tipo var nunca
        //asi cuando java compila sabe cual usar
        this.a = a; //this apunta al atributo, lo uso ccuando uso variables identicas
        this.b = b; // this.b es el hit
        System.out.println("Se esta ejecutando este constructor número dos");
    }
    
    //Metodo comienzo con el modificador de acceso = public void=vacio (hay otros)
    public void sumarNumeros(){ //este no devuelve solo imprime 
        int resultado = a+b;
        System.out.println("resultado ="+resultado); //no llame al metodo solo imprimi en consola
    
    }
    //Otro metodo que retorna el valor 
    public int sumarConRetorno(){ //aqui esta vacio
        //int resultado = a + b; //aca inicio una variable tambien de tipo entero
        return a + b; //lo mismo mas corto
    }
    // tipo de acceso "public" tipo de retorno "int" luego nombre 
    public int sumarConArgumentos(int arg1, int arg2){ //int a y int b son los argumentos
        // a = arg1; //seria una variable con el atributo (lo que toma naranja es el atributo ej "a")
        // b = arg2; //pueden tener el mismo nobre pero el programa los diferencia
        //return a + b; //hacemos un regreso de la suma
        
        //"this" apunta al lugar donde esta grabado para modificarlo
        this.a = arg1; //El argumento a se asigna al atributo this.a
        this.b = arg2; //pongo this. y se despliegan las opciones
        //return a + b;
        return this.sumarConRetorno(); //dentro de un metodo uso otro metodo 
        //sumarConRetorno (siempre que sea de la misma clase)
    }
}
//Proyecto siempre PascalCase
//Paquete en minuscula
//