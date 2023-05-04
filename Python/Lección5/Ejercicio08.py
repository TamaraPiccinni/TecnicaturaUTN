# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones:
#           1. Ingresar dinero en la cuenta
#           2. Retirar dinero de la cuenta
#           3. Mostrar dinero disponible
#           4. Salir

saldo = 1000
while True:
    print("\t. :MENÚ:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opción de menú: "))
    print()
    if opcion == 1:
        monto = float(input("Digite el monto a ingresar: "))
        saldo += monto
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == 2:
        retiro = float(input("Digite el monto a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Su saldo actual es: ${saldo}")
        else:
            print("No tiene dinero suficiente")
            print(f"Su saldo actual es: ${saldo}")
    elif opcion == 3:
        print(f"Su saldo es: ${saldo}")
    elif opcion == 4:
        print("Gracias por usar el cajero automatico")
        break
    else:
        print("Error de opción de menú")
        print()



