'''
miVariable = 3
print(miVariable)
miVariable = "hello world"
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# las literales se escriben x680

# Tipos int,float,string,Bool
a = 10
print(a)
print(type(a))
a = 14.5
print(a)
print(type(a))
a = "hola"
print(a)
print(type(a))
a = True
print(a)
print(type(a))
a = False
print(a)
print(type(a))

# Manejo de cadenas (string)
miGrupoFavorito = "Los Ustedes"
caracateristicas = "The best"
print("Mi grupo favorito es: ", miGrupoFavorito, caracateristicas)

# number1 = "7"
# number2 = "8"
# print(number1+number2)
# print(int(number1)+int(number2))

# Tipos Datos Boleanos (bool)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion input()
resultado = input("Digite un numero: ")  # regresa un dato tipo string
print(resultado)

# Conversion de la entrada de datos
number1 = int(input("Escribe el priemer numero: "))
number2 = int(input("Escribe el segundo numero: "))
resultado = number1+number2
print("El resultado de la suma es: ", resultado)
'''
"""
# 27/4
operandoA= 8
operandoB= 5
suma = operandoA + operandoB
# print(f*resultado de la suma :", suma) # f interpolacion
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicacion es: ´{multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la division (int) es: {division}")

modulo = operadorA % operadorB
print(f"El resultado de la division o residuo (modulo) es: {modulo}")
"""
'''
alto = int(input("Proporcione el alto del rectángulo: "))
ancho = int(input("Proporcione el ancho del rectángulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print("Área:", area)
print("Perimetro: ", perimetro)
'''
"""
miVariable3 = 10
print(miVariable3)

# operadores de reasignasion
miVariable3 = miVariable3 + 1
print(miVariable3)

# mas corto
miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)
miVariable3 *= 3
print(miVariable3)
miVariable3 /= 2
print(miVariable3)
"""
'''
# operadores de comparacion
d = 4
b = 2
resultado = d == b  # comprobamos si son iguales
print("=", resultado)

# operador diferente
resultado = d != b
print("diferentes", resultado)

# operador mayor que
resultado = d > b
print("mayor", resultado)

# operador menor que
resultado = d < b
print("menor", resultado)

# operador menor o igual
resultado = d <= b
print("menor o igual", resultado)

# operador mayor o igual
resultado = d >= b
print("mayor o igual", resultado)
'''
"""
numero = int(input("Proporcione un numero: "))
print(f"El residuo de la division es {numero % 2}")
if numero % 2 == 0:
    print(f"El valor del numero es {numero} Es par")
else:
    print(f'El valor del numero es: {numero} Es impar')
"""
'''

edadAdulto = 18
edadPersona = int(input("Proporcione su edad: "))
if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, usted es menor de edad")
'''
"""
# operadores logicos
a = True
b = False
resultado = a and b
print("verdadero o falso:", resultado)

# operador or
resultado = a or b
print("o:", resultado)

# operador not
resultado = not a
print("not: ", resultado)
"""
"""
#Ejerciocios
# Valor dentro de un rango
num = int(input('ingrese un numero: '))
if num >= 0 and num <= 5:
    print(f"{num} el valor esta dentro del rango")
else:
    print(f"{num} el valor esta fuera del rango")
"""
'''
# operador or
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else: print("No puede asistir, tiene trabajo que hacer")

# Rango de edad
edad = int(input('ingrese la edad: '))
if edad >= 20 and edad <= 30:
    print(f"{edad} el valor esta dentro del rango")
else:
    print(f"{edad} el valor esta fuera del rango")

edad = int(input("Ingrese su edad: "))
if (edad<=29 and edad>=20) or (edad<=39 and edad>=30):
        print(f"La edad esta dentro del rango")
else: print(f"La edad esta fuera del rango")

# valor de 2 numeros (cual es mayor)
num = int(input('ingrese un numero: '))
num2 = int(input('ingrese un numero: '))
if num > num2:
    print(f"{num} es mayor a {num2}")
else:
    print(f"{num2} es mayor a {num}")
'''
'''
# tienda de libros
print("Ingrese los suguientes datos del libro:")
nombre = input("digite el nombre del libro:")
id = int(input("digite el ID del libro:"))
precio = float(input("digite el precio del libro:"))
envioGratuito = input("Indicar si el libro tiene envio gratis (True o False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True/False"

print(f"""
      nombre: {nombre}
      id: {id}
      precio: {precio}
      envio Gratuito?: {envioGratuito}
""")
#probando los arreglos de git
'''
