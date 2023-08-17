
package domain;

public class Persona {
    //Atributos de herencia
    protected String nombre; //protected en ves de private para que se herede a las clases hijas en cualquier paquete
    protected char genero;
    protected int edad;
    private String direccion;
    
    //Constructo vacio: este es para crear objetos sin necesidad de inicializar 
    //los atributos
    //para constructores el modificador de acceso de ser publico 
    // y el nombre se llama igual a la clase
    public Persona() {        
    }
    //constructor2
    public Persona(String nombre){ 
        this.nombre = nombre;
    }

    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }
    public String getDireccion() {
        return this.direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public char getGenero() {
        return this.genero;
    }

    public void setGenero(char genero) {
        this.genero = genero;
    }

    public int getEdad() {
        return this.edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    @Override //sobreescritura describe el metodo to String
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Persona{nombre=").append(nombre);
        sb.append(", genero=").append(genero);
        sb.append(", edad=").append(edad);
        sb.append(", direccion=").append(direccion);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}
