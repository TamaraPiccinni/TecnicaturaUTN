# Ejercicio 2: Función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumentos

#Definimos la función para multiplicar
def multiplicar_valor(*args): #recibimos cantidad de parametros indefinidos
#    pass #es para seguir programado saliendo de la funcion
    resultado = 1 #0 x cualquier número es 0 por eso inicio en 1
    for valor in args: # iteramos cada elemento
        resultado *= valor
    return resultado

#llamamos a la funcion
print(multiplicar_valor(3, 5, 9, 2, 1)) #3,5,9,2,1 son los argumentos