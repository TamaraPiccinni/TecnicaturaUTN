/*
Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se han introducido
lo hacemos primero con la clase Scanner
luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, contador = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >=0){
            JOptionPane.showMessageDialog(null,"El numero:"+numero+" es POSITIVO");
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null,"Has introducido: "+contador+" numeros positivos");
    }
}