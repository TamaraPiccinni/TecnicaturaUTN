package domain;

import java.util.Date;

public class Cliente extends Persona{ /*extends para que la calse hija cliente 
    herede de la clase padre Persona */
    //Atributos (de manera pribada xq la clase cliente no va a tener hijas
    private int idCliente;
    private Date fechaRegistro; //Importar la clase Date
    private boolean vip; //Very important person
    private static int contadorCliente; //Tipo estático
    
    //Constructor 
    public Cliente(Date fechaRegistro, boolean vip, String nombre,
            char genero, int edad, String direccion){
        super(nombre, genero, edad, direccion); /*contructo super de la clase 
        padre(en primer lugar)*/
        this.idCliente = ++Cliente.contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }
//insert code getter and setters
    public int getIdCliente() {
        return this.idCliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() { //is xq es booleano
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }
// insert code to String 
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder(); // xq asi es mas eficiente
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}
//en TestHerencia crear e importar la clase cliente y crear un nuevo objeto
//(nos devuelve la fecha actual) y el valor boolean, nombre, genero, edad, 
//diereccion) 