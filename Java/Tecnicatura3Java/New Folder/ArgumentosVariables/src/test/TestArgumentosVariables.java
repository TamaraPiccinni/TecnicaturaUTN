
package test;

public class TestArgumentosVariables {
    public static void main(String[] args) {
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Juan", "Perez", 7, 8, 9);
        
    }
    private static void variosParametros(String nombre,String apellido,int ...numeros){ // los argumentos son enteros int
        //... es lo variable que es indefinido, siempre al final
        //esto se va a convertir en un arreglo
        System.out.println("Nomre: "+nombre+", Apellido: "+apellido);
        
        imprimirNumeros(numeros);
    }
     private static void imprimirNumeros(int...numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: "+numeros[i]);
        }
     }
}
