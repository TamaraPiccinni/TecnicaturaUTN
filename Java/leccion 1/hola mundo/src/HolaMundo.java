
import java.util.Scanner;

public class HolaMundo {
public static void main(String[] args) {
    /*System.out.println("Hola mundo desde Java");
    
    int miVariable = 10;
    System.out.println(miVariable);
    miVariable=5;
    System.out.println(miVariable);
    //Tipo Sting 
    String miVariableCadena = "Bienvenidos";
    System.out.println(miVariableCadena);
    miVariableCadena = "Sigamos creciendo en programación";
    System.out.println(miVariableCadena);
*/
    //Var - Inferencia de tipo en Java
    /*
    var miVariableEntera2 = 10;
    var miVariableCadena2 = "Seguimos estudiando";
    System.out.print("miVariableEntera2 = "+ miVariableEntera2);
    System.out.print("miVariableCadena2 = "+ miVariableCadena2);
    //soutv + tab
    //Para ejecutar shift+f6
        
    //Reglas par a definir ua variable en JAva
    //se puede usar cualquier letra pero se recomienda camelCasse mas facil comprension
    // y se puede usar el signi _ y el $ y acentos tambien se puede, pero no se recomienda
    var miVariableEjemplo = 45;
    
    var usuario = "Tamara";
    var titulo = "Estudiante";
    var union = titulo + " " + usuario;
    System.out.println("union = " + union);
    
    var a = 8;
    var b = 4;
    System.out.print(usuario + (a +b)); //sino pongo a + b entre parentesis lo concatena de izq a derecha, no suma xq 1º hay una cadena
    
    //Ejercicio: Caracteres Especiales con Java
    
    var nombre = "Tamara";
    System.out.println("\nNueva lienea: \n" +nombre); // diagonal inversa + n;
    System.out.println("Tabulador: \t"+ nombre);  //Tabulador un espacio para centrar
    System.out.println("\t\t, :MENÚ:.");
    System.out.println("Retroseso: \b\b"+nombre); //Caracter de Retroseso
    System.out.println("comillas simples: \'"+nombre+"\'");
    System.out.println("Comillas Dobles: \""+nombre+"\"");
    */
    /*
    //Clase Scanner
    Scanner entrada = new Scanner(System.in); //hay que importarla para que no de error
    System.out.println("Digite su numbre:");
    var usuario2 = entrada.nextLine(); //un metodo para leer una linea completa que recibio del ususario
    //var ususario2 = "Carlos";
    System.out.println("usuario2 = " + usuario2);
    System.out.println("Escriba el titulo: ");
    var titulo2 = entrada.nextLine();
    System.out.println("Escriba el autor");
    String autor = scanner.nextLine();
    System.out.println (titulo2 + "fue escrito por: "+autor2);
    System.out.println("Resultado: "+titulo2+" "+usuario2);
    /*
    byte numEnteroByte = 127;
    System.out.println("numEnteroByte - " + numEnteroByte);
    System.out.println("valor minimo del byte:" + Byte.MIN_VALUE);
    System.out.println("Valor maximodel byte" + Byte.MAX_VALUE);
    
    //Short numEnteroShort = (short)32768; si pongo un numero mayor da error si agrego el (short) no salta error pero pierde presicion y da negativo
    Short numEnteroShort = 32767;
    System.out.println("numEnteroShort - " + numEnteroShort);
    System.out.println("valor minimo del Short:" + Short.MIN_VALUE);
    System.out.println("Valor maximodel short" + Short.MAX_VALUE);
    
    //int numEnteroInt = (int)2147483647L; (no salta error pero lo muestra en negativo debo agregar la L para que no salte a demas del int
    int numEnteroInt = 10;
    System.out.println("numEnteroInt - " + numEnteroInt);
    System.out.println("valor minimo del Int:" + Integer.MIN_VALUE);
    System.out.println("Valor maximodel Int" + Integer.MAX_VALUE);
    
    long numEnteroLong = 9223372036854775807L; //Es el maximo entero (agrego L para que no de error), si quiero un numer fmayor se usan n flotantes
    System.out.println("numEnteroLong - " + numEnteroLong);
    System.out.println("valor minimo del Long:" + Long.MIN_VALUE);
    System.out.println("Valor maximodel Long" + Long.MAX_VALUE);

    float numFloat = 10.0F; //usar mayusculas para mejor comprension, minuscula acepta pero confunde
    //si ponemos un decimal, hay que agregar F para que indique que la literal es float
    // otra forma es indicar al compilador que lo tome  com flotante poninedo (float)
    // se pueden usar ambos o uno solo (float)10F;
    //float numFloat = (float)3.4028236E38D;
    // Si uso un num mayor da error se arregla (float) + D
    System.out.println("numFloat - " + numFloat);
    System.out.println("valor minimo del Float: " + Float.MIN_VALUE);
    System.out.println("Valor maximodel Float: " + Float.MAX_VALUE);
    
     double numDouble = 10;
    System.out.println("num - " + numDouble);
    System.out.println("valor minimo del Double: " + Double.MIN_VALUE);
    System.out.println("Valor maximodel Double: " + Double.MAX_VALUE);
    */
    /*
    Inferencia de tipos va y tipos primitivos
    */
    /*
    var numEntero = 20; // Las literales automaticamente son de tipo int
    System.out.println("numEntero = " + numEntero);
    var numFloat = 10.0F; // Automaticamente con el puento se transforma en tipo double (F lo toma como float)
    System.out.println("numFloat = " + numFloat);
    var numDouble = 10.0; //
    System.out.println("numDouble = " + numDouble);
    char miVaraiableChar = 'a';
    System.out.println("miVaraiableChar = " + miVaraiableChar);
    
    char varCaracter = '\u0024'; // Indicamos a java con el valor del codigo unicode
    System.out.println("varCaracter = " + varCaracter);
    
    char varCaracterDecimal = 36; // valor decimal del juego de caracteres unicode
    System.out.println("varCaracterDecimal = " + varCaracterDecimal);
    
    char varCaracterSimbolo = '$'; // Un caracter especialm podemos copiar y pegar desde unicode
    System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
    
     var varCaracter1 = '\u0024'; // Indicamos a java con el valor del codigo unicode
    System.out.println("varCaracter1 = " + varCaracter1);
    
    var varCaracterDecimal1 = (char)36; // valor entero y le asigna un tipo int, agrego char para que si lo tome
    System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
    
    var varCaracterSimbolo1 = '$'; // Un caracter especialm podemos copiar y pegar desde unicode
    System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
    
    int varEnteroChar = '$';
    System.out.println("varEnteroChar = " + varEnteroChar);
    int caracterChar = 'b';
    System.out.println("caracterChar = " + caracterChar);
*/
    /*
    //Tipos primitivos tipos booleanos true o false
    boolean varBool = true;
    System.out.println("varBool =" + varBool);
    
    //if (varBool == true) no hace falta por true
    
    if(varBool){
        System.out.println("La bandera es verde");
    }
    else{
        System.out.println("La bandera es roja");
    }
    //Algoritmo : ¿Es mayor de edad?
    
    var edad = 30; //Literal tener presente la interderencia de los tipo
   // var adulto = edad>=18; //Esta es una expresion booleana
    if(edad>=18){ //haciendo así acortamos y lo hacemos mas eficiente
        System.out.println("Eres mayor de edad");
    }
    else{
        System.out.println("eres menor de edad");
        }
*//*
    //Conversion de tipos primitivos (cadena a tipo entero y viceversa)
    var edad = Integer.parseInt("20");
    System.out.println("edad = "+ (edad+1));
    }
    */
/*
    var edad = "20";
    System.out.println("edad = " + (edad+1));
    var valorPI = Double.parseDouble("3.1416");
    System.out.println("valorPI =" +valorPI);
    */
    //Pedir un valor
    //var entrada = new Scanner(System.in);
    /*System.out.println("Digite su edad:");
    edad = Integer.parseInt( entrada.nextLine());
    System.out.println("edad = "+edad);
*/
    //conversion de tipos primitivos Java parte 2
    /*var edadTexto = String.valueOf(10);
    System.out.println("edadTexto = "+edadTexto);

    var freseChar ="programadores".charAt(4);
    System.out.println("freseChar = " + freseChar);
    
    System.out.println("Digite un caracter: ");
    freseChar = entrada.nextLine().charAt(0);
    System.out.println("freseChar = " + freseChar);
    */
    /*
    //sguimos con operadores de asignacion
    int num1 = 5, num2 = 4; //inicio una variable y asigno un valor de tipo entero (int)
    //si quiero poner inferencia de tipos (var) debo hacelo en 2 lineas
    var solucion = num1 + num2; //aca no esta concatenando solo es una operacion aritmetica
    System.out.println("solucion = " + solucion);
    
    solucion = num1 - num2;
    System.out.println("solucion de la resta= " + solucion);
    
    solucion = num1 * num2;
    System.out.println("solucion de la multiplicacion = " + solucion);
    
    solucion = num1 / num2;
    System.out.println("solucion de la division= " + solucion);
    
    var solucion2 = 3.4  / num2;
    System.out.println("solucion2 usando valor flotante= " + solucion2);
    
    solucion = num1 % num2; // Guarda el residuo entero de la division no el resultado
    System.out.println("solucion = " + solucion);
    if (num1 % 2 == 0)
        System.out.println("es un numero par");
    else 
        System.out.println("es un numero impar");
    // no uso llaves en este if xq use una sola linea dentro de cada bloque
    */
    /*
    int varNum1 = 1, varNum2 = 4; // operador de asigancion que estoy usando es el =
    int varNum3 = varNum1 + 6 - varNum2; // una operacion
    System.out.println("varNum3 =" + varNum3);
    
    varNum1 +=1; // es lo mismo varNum1 = varNum1 +1;
    System.out.println("varNum1 = " + varNum1);
    
    // hacaerlo con  - * / %
    varNum2 -=2;
    System.out.println("varNum2 = " + varNum2);
        
    varNum1 *=5;
    System.out.println("varNum1 = " + varNum1);
    
    varNum3 /=4;
    System.out.println("varNum3 = " + varNum3);
    
    varNum1 %=6;
    System.out.println("varNum1 = " + varNum1);
    */
}
}


