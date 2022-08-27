
package CicloWhile;

public class EjercicioWhile {
    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while(conteo<7){
            System.out.println("conteo =" + conteo);
            conteo++; //Vamos aumentanodo en uno la variable
        }
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while (contador < 7); //si pongo <=7 mostrara el 7 pero seran 8 nun no 7
    // while es mientras hacer y do while es repetir hasta que
    
    //for (aqui declara la variable; es la condicion; es el incremento ){
    for (var contando = 0; contando <7; contando++){
        System.out.println("contando = " + contando);
        
    }
    }
}
