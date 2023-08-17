
package PasoPorValor;

public class PasoPorValor {
    public static void main(String[] args) {
        var valorX = 20;
        System.out.println("valorX = " + valorX);
        cambioValor(valorX);//Solo le enviamos una copia
        System.out.println("valorX = " + valorX);
    }
    
    public static void cambioValor(int arg1){ //Parámetro por valor es una copia
        System.out.println("arg1 = " + arg1);
        arg1 = 15; //no lo modifica solo sigue copiando xq es otro espacio de memoria
        //como no lo paso como referencia no lo toma, sino no retorna nada
    }
}
