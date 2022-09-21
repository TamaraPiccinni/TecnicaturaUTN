#Ejercicio 01: Crear una funcion para sumar los valores recibidos de tipo
#numericos, utlizamos argumentos variables *args como parametro de la
#Funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def sumar_valor(*args): #recibimos cantidad de parametros indefinidos
#    pass #es para seguir programdo saliendo de la funcion
    resultado = 0
    for valor in args: # iteramos cada elemento
        resultado += valor
    return resultado

#llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1)) #3,5,9 son los argumentos