class GrupoScout:
    def __init__(self):
        self.integrantes = 0
        self.mes = 0
        self.vporcentaje = [0] * 100
        self.vedad = [0] * 100 #cambiar a fecha de nacimiento
        self.vdni = [0] * 100
        self.datos = [[0] * 100 for _ in range(100)]
        self.nombre_completo = [None] * 100
        self.presente = [None] * 100
        self.ausente = [None] * 100
        self.vramas = [None] * 100
        self.vnombres = [None] * 100

    def mostrar_menu(self):
        print("-------------------  MENU  -------------------\n"
              "| 1. Cargar datos                              |\n"
              "| 2. Cargar asistencias                        |\n"
              "| 3. Mostrar la matriz con toda la informacion |\n"
              "| 4. Mostrar el porcentaje de asistencias      |\n"
              "| 5. salir                                     |\n"
              "' ----------------------------------------------\n\n"
              "Elegir la opción deseada: ")

#clase integrantes
    def pedir_datos(self):
        cantidad_integrantes = int(input("Digite la cantidad de integrantes: "))

        for i in range(cantidad_integrantes):
            print("Digite apellido y nombre completo: ")
            self.vnombres[i] = input()
            print("Ingrese su edad: ")
            self.vedad[i] = int(input())
            print("Ingrese DNI: ")
            self.vdni[i] = int(input())

        self.integrantes = cantidad_integrantes

#clase fecha
    def pedir_mes(self):
        mes = int(input("Ingrese el mes que desea cargar: "))
        return mes

    def seleccionar_mes(self, mes):
        if mes == 12:
            return 3
        elif mes == 4 or mes == 7 or mes == 10:
            return 5
        else:
            return 4
#metodo asistencia
    def asistencia(self):
        cant_sabados = self.seleccionar_mes(self.mes)

        for j in range(self.integrantes):
            print(f"Digite la cantidad de asistencias del integrante: {self.vnombres[j]} DNI {self.vdni[j]}")

            suma = 0
            for k in range(cant_sabados):
                while True:
                    print(f"{k + 1}° Sabado mes {self.mes}: Presente(1) - Ausente(0): ")
                    asist = int(input())
                    if asist == 0 or asist == 1:
                        break

                suma += asist
                self.datos[j][self.mes - 4] = suma

            print(f"El integrante {self.vnombres[j]} tiene {suma} asistencias y {cant_sabados - suma} inasistencias")

    def mostrar_matriz(self):
        print(" -------------------------------------------------------")
        print("               Asistencia Anual Scout 2023\n\n")
        print("  NOMBRE   DNI    RAMA   MES: 4  5  6  7  8  9 10 11 12")

        for i in range(self.integrantes):
            print("\n")
            print(f"    {self.vnombres[i]}  {self.vdni[i]}  {self.vramas[i]}")
            for j in range(9):
                print(f" {self.datos[i][j]}")

        print("\n\n")

    def poner_cero_matriz(self):
        for i in range(100):
            for j in range(9):
                self.datos[i][j] = 0

    def poner_cero_vector(self):
        for i in range(100):
            self.vedad[i] = 0
            self.vdni[i] = 0
            self.vnombres[i] = 0

#atributo del integrante
    def definir_rama(self):
        for i in range(self.integrantes):
            if self.vedad[i] <= 10:
                self.vramas[i] = "Manada   "
            elif self.vedad[i] <= 13:
                self.vramas[i] = "Unidad    "
            elif self.vedad[i] <= 17:
                self.vramas[i] = "Caminantes"
            elif self.vedad[i] <= 21:
                self.vramas[i] = "Rovers    "
            else:
                self.vramas[i] = "Adultos   "

    def calculo_porcentaje(self):
        for i in range(self.integrantes):
            suma = sum(self.datos[i][:9])
            self.vporcentaje[i] = suma

    def mostrar_matriz_porc(self):
        print("---------------------------------------------------------------")
        print("        	     Porcentaje de Asistencia Anual Scout ")
        print("---------------------------------------------------------------")
        print("                		 	 MESES 2023\n")

        print("       4    5   6   7   8   9  10  11  12    Porcentaje Anual")

        for i in range(self.integrantes):
            print("\n")
            print(self.vnombres[i])
            suma = 0
            for j in range(9):
                mes = j + 4
                k = self.seleccionar_mes(mes)
                print(f" {(self.datos[i][j] / k) * 100}%")
                suma += self.datos[i][j] / k

            print(f" {(suma / 9) * 100}%")
            print("\n\n")

    def ejecutar(self):
        salir = False
        while not salir:
            self.mostrar_menu()
            opcion = int(input())

            if opcion == 1:
                self.pedir_datos()
                self.definir_rama()
            elif opcion == 2:
                self.mes = self.pedir_mes()
                self.asistencia()
            elif opcion == 3:
                self.mostrar_matriz()
            elif opcion == 4:
                self.calculo_porcentaje()
                self.mostrar_matriz_porc()
            elif opcion == 5:
                salir = True
            else:
                print("Se equivocó de número")

        print("Fin del menú")


if __name__ == '__main__':
    grupo_scout = GrupoScout()
    grupo_scout.ejecutar()
