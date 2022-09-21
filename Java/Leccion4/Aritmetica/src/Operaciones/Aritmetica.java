/* Atributos y metodos empiezan con minuscula (camelCase
clase se empeiza con mayuscual PascalCase
*/
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a; //por default es 0 (al no inicializarla int es 0, bolleano es false) 
    int b; //no estan vacias, tienen el valor default
    //metodo comienzo con el modificador de acceso = public void=vacio (ahy otros)
    public void sumarNumeros(){
        int resultado = a+b;
        System.out.println("resultado ="+resultado); //no llame al metodo solo imprimi en consola
        
    }
}
