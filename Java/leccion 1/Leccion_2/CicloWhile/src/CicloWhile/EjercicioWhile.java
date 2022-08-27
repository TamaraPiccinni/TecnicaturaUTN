
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
    for (var contando = 0; contando <7; contando++){ //aqui pongo la llave xq si es mas de una linea la necesita
        if (contando % 2 == 0){
            System.out.println("contando = " + contando);
            //for(int i=1;i!=0;i++){ System.out.println("Print eterno"); } esta es una forma correcta,  ya que siempre va a ser entero
            break;
            }
        }
    
    for (var contando = 0; contando <7; contando++){ //aqui pongo la llave xq si es mas de una linea la necesita
        if (contando % 2 != 0){
            continue; //va a la sig interaccion
            }
            System.out.println("contando = " + contando);
        }
    }
}
