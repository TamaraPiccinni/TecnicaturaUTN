#Ejercicio 11: Agenda telefonica
#hacer un programa que simule una agenda de contactos.
#Crear un diccionario donde la clave sea el nombre del usuario
#y el valor sea el teléfono, el programa tendrá el siguiente menú de opciones
#   1. Nuevo contacto
#   2. Borrar contacto
#   3. Ver contactos existentes
#   4. Salir

#nombreDeUsuario = input("Ingrese su nombre de usuario: ")
#clave = nombreDeUsuario
agenda = {}
while True:
    print()
    print("\t MENÚ")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    print()
    opcion = int(input("Digite una opcion del menú: "))
    print()
    if opcion == 1:
        nombre = input("Digite el nombre: ")
        telefono = input("Digite el número de teléfono: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print("El contacto fue agregado")
        else:
            print("Este contacto ya existe")
    elif opcion ==2:
        nombre = input("Digite el nombre que desea borrar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print(f"Se ha eliminado: {nombre}")
        else:
            print("No existe ese contacto")
    elif opcion ==3: #agregar un if en caso que este vacia la lista
        print("Lista de contactos")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, Teléfono: {valor}")
    elif opcion ==4:
        print("\t Muchas Gracias")
        break
    else:
        print("Error se equivoco de opción de menú")