
package mundopc;

import ar.com.system2023.mundopc.*; //Cambio el .Monitor x el * 
//para que se importen todas las clases

public class mundoPc {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13);//Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP,
                tecladoHP, ratonHP); //creo objeto computadora y le agrego 
                //todos los parametros
                
        //Creo mas objetos de otras marcas y luego un objeto de tipo orden
        Monitor monitorGamer = new Monitor("Gamer", 32);//Importar la clase
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        
        Computadora computadoraGamer = new Computadora("Computadora Gamer", 
                monitorGamer, tecladoGamer, ratonGamer); //creo objeto 
                //computadora y le agrego todos los parametros
        
        //*Tarea mas objetos
        Monitor monitorSamsung = new Monitor("Samsung", 40);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", 
                monitorSamsung, tecladoSamsung, ratonSamsung);          
        
        Monitor monitorLG = new Monitor("LG", 16);
        Teclado tecladoLG = new Teclado("Cable", "LG");
        Raton ratonLG = new Raton("Cable", "LG");
        
        Computadora computadoraLG = new Computadora("Computadora LG", 
                monitorLG, tecladoLG, ratonLG);

        Monitor monitorApple = new Monitor("Apple", 42);
        Teclado tecladoApple = new Teclado("Bluetooth", "Apple");
        Raton ratonApple = new Raton("Bluetooth", "Apple");
        
        Computadora computadoraApple = new Computadora("Computadora Apple", 
                monitorApple, tecladoApple, ratonApple); 
        
        Monitor monitorRazer = new Monitor("Computadora Razer", 30);
        Teclado tecladoRazer = new Teclado("Bluetooth", "Razer");
        Raton ratonRazer = new Raton("Bluetooth", "Razer");
        
        Computadora computadoraRazer = new Computadora("Computadora Razer", 
                monitorRazer, tecladoRazer, ratonRazer);
        
        Monitor monitorAsus = new Monitor("Asus", 20);
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        
        Computadora computadoraAsus = new Computadora("Computadora Asus", 
                monitorAsus, tecladoAsus, ratonAsus);
        
        Monitor monitorLenovo = new Monitor("Lenovo", 16);
        Teclado tecladoLenovo = new Teclado("Cable", "Lenovo");
        Raton ratonLenovo = new Raton("Cable", "Lenovo");
        
        Computadora computadoraLenovo = new Computadora("Computadora Lenovo", 
                 monitorAsus, tecladoAsus, ratonAsus);
        
        Monitor monitorDell = new Monitor("Dell", 13);
        Teclado tecladoDell = new Teclado("Cable", "Dell");
        Raton ratonDell = new Raton("Cable", "Dell");
        
        Computadora computadoraDell = new Computadora("Computadora Dell", 
                 monitorDell, tecladoDell, ratonDell);
        
        //Computadora computadoraXMayor = new Computadora("Computadora por Mayor", 
        //        monitorGamer, tecladoGamer, ratonGamer, monitorApple, tecladoApple, ratonApple);
        
        Monitor monitorAcer = new Monitor("Acer", 13);
        Teclado tecladoAcer = new Teclado("Cable", "Acer");
        Raton ratonAcer = new Raton("Cable", "Acer");
        
        Computadora computadoraAcer = new Computadora("Computadora Acer", 
                 monitorAcer, tecladoAcer, ratonAcer);
        
        CPU cpu = new CPU("XFX");
        /*Parlante = new Parlante("Edifier");
        Pad = new Pad("Genius");
        Camara = new Camara("Logitech");
        Fuente = new Fuente("TVR");
        PlacaMadre = new PlacaMadre("Asus");
        Procesador = new Procesador("Intel I9");
        Disco = new Disco("1 TB");*/
        
        
        
        Computadora computadoraXMayor = new Computadora("Computadora Acer", 
                monitorAcer, tecladoAcer, ratonAcer);
        
        
        //objeto tipo orden
        Orden orden1 = new Orden(); //Iniciamos vacio
        Orden orden2 = new Orden(); //nueva lista
        
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadoraSamsung);
        orden1.agregarComputadora(computadoraLG);
        orden1.agregarComputadora(computadoraApple);
        orden1.agregarComputadora(computadoraRazer);
        orden1.agregarComputadora(computadoraAsus);
        orden1.agregarComputadora(computadoraLenovo);
        orden1.agregarComputadora(computadoraDell);
        orden1.agregarComputadora(computadoraXMayor);
        
        Computadora computadorasVarias = new Computadora("Computadora de "
                + "diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        orden2.agregarComputadora(computadorasVarias);
        
        
        
        orden1.mostrarOrden();
        orden2.mostrarOrden();        
    }
    
}
/*Crear mas objetos de tipo computadora con todos sus elementos
completar una lista en el objeto orden1 que llegue a los 10 elementos
probar de esta manera como funcionan los métodos al máximo rendimiento*/