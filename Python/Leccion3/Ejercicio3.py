"""
Clase 9
Ejercicio 3
Leer 10 numero e imprimir cuantos son positivos. cuantos negativos y cuantos neutros
"""

conteoPositivo = 0
conteoNegatico = 0
conteoNeutros = 0

for i in range(10):
    num= float(input("Digite un numero: "))
    if num == 0:
        conteoNeutros += 1
    elif num>0:
        conteoPositivo += 1
    else:
        conteoNegatico += 1
print(f"\nLa cantidad de positivos es: {conteoPositivo} \n"
      f"La cantidad de negativos es: {conteoNegatico} \n"
      f"La cantidad de neutros es: {conteoNeutros} ")


