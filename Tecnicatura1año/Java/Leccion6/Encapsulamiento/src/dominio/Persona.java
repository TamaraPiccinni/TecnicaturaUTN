
package dominio;

public class Persona {
    //atributos
    private String nombre; //tipo String no entra en primitivos x eso en mayuscula
    private double sueldo; //doubles es primitivo x eso va en minuscula
    private boolean eliminado;
            
    /*constructor debe ser el mismo nombre, si la classe es privada solo puede acceder 
    desde los metodos, y por eso lo hago publico
    */
    public Persona(String nombre, double sueldo, boolean eliminado){ //nombre, sueldo y eliminado son las variables
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.eliminado = eliminado;
        
    }
    //definimos, creamos metodos get y set (click derecho o alt+insert)
    //para poder acceder hay que crear uno x cada variable

    public String getNombre() { //retorna nombre 8el valor del atributo nombre
        return nombre;
    }

    public void setNombre(String nombre) { //necesita un parametro y devuelve la modificacion al atributo
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    public boolean isEliminado() { //en ves de get usa is (xq es una pregunta)
        return eliminado;
    }

    public void setEliminado(boolean eliminado) {
        this.eliminado = eliminado;
    }
    
}
