'''
Ejercicio 1
debemos plasmar la expresion en una expresion algoritmica,
osea en codigo

'''
'''

a = float(input('Digite el valor de a:'))
b = float(input('Digite el valor de b: '))
c = float(input('Digite el valor de c: '))

resultado = (a**3*(b**2-2*a*c))/(2*b)
print(f'El resultado es : {resultado}')
'''

'''
#Ejercicio 3
# Intercambiar el valor de dos variables.
# Por ejemplo:
# a = 10        a = 5
# b = 5         b = 10

a = int(input('Digite el valor de a: '))
b = int(input('Digite el valor de b: '))

a, b = b, a

print(a)
print(b)
'''
'''
#jercicio 4
# Área y longitud de un circulo
# Hacer un programa para ingresar el radio de un circulo
# y se reporte su área y la longitud de la circunferencia.
# Área = Pi * r2
# Longitud = 2 * Pi * r
# En este ejercicio vamos a necesitar importar el modulo math
# porque tiene el valor de Pi
# Se escribe:   import math

import math
radio = float(input('Digite el valor de radio: '))
area = math.pi * (radio**2)
longitud = 2 * math.pi * radio
print(f'El área del círculo es: {area:.2f}') # .2f es para que l muestre con 2 decimales
print(f'La longitud del círculo es: {longitud:.2f}')
'''