#Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
#numericos, utilizamos argumentos variables *args como parámetro de la
#Funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos.

def sumar_valor(*args): #recibimos cantidad de parámetros indefinidos
#   pass (es para seguir programado saliendo de la función)
    resultado = 0
    for valor in args: # iteramos cada elemento
        resultado += valor
    return resultado

#llamamos a la funcion
print(sumar_valor(3, 5, 9, 2, 1)) #3,5,9,2,1 son los argumentos