# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
# 5
# 4
# 3
# 2
# 1
# En caso de ser el número 3 debe imprimir:
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada
def numeros_recursivos(numero):
    if numero >= 1: # Caso Base
        print(numero)
        numeros_recursivos(numero-1) # Caso Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
         print('Valor incorrecto')

imprimirNumero = int(input('Digite el numero: '))
resultado = numeros_recursivos(imprimirNumero) # Lo hacemos en código duro
print(f'El oreden desendente del número {imprimirNumero} es: {resultado}') # Tarea que el usuario ingrese el número para calcular el factorial
