
package ar.com.system2023.mundopc;

public class CPU extends DispositivoEntrada{
    private final int idCPU;
    private static int contadorCPU;
    
    /*Constructor*/
    public CPU(String tipoEntrada, String marca){
        super(tipoEntrada, marca);
        this.idCPU = ++CPU.contadorCPU;
    }

    @Override
    public String toString() {
        return "CPU{" + "idCPU=" + idCPU +super.toString()+'}';
    }
    
}
