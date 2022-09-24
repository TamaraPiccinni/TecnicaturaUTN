
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
    //creamos un objeto llamado aritmetica1 que trabaja en el espacio de memoria del constructor
    //Aritmetica() llamamos a la clase =al constructor y reserva espacio de memoria
        Aritmetica aritmetica1 = new Aritmetica(); 
        aritmetica1.a = 3; //aca modifico el valor de los atrubitos por medio del . 
        aritmetica1.b = 7; // objeto aritmetica1 usando el operador de . "punto"
        aritmetica1.sumarNumeros();
    
        //pruebo el metodo con sumar con retorno
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);
    
        //vamos a llamar a travez del objeto con el operador de punto al metodo sumarConRetorno
        //damos 2 argumentos del tipo entero
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = "+resultado);
    }
}
