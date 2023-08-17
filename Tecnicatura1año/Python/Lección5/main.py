#Comenzamos con funciones

#mi_funcion() no se puede llamar antes de definirla

#Definimos una función se usa snake_casse o camelCasse
# con snake_casse para practicar. los () son necesarios

def mi_funcion(): #para identificar esta funcion usamos ()
    print('Feliz dia del programador')

mi_funcion()  #llamamos la funcion
mi_funcion() #se puede llamar N cantidad de veces

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+ ' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #pasamos uno por uno los datos de la Lista a la función
show(*person) #Esto es lo mismo que lo anterior, pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #desempaquetamos a través de una Tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"} # Diccionario
show(**person3) #** usamos dos porque recorre 2 elementos (clave y valor)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:#agrego if
        break # Esta es la única manera para que no se ejecute el else
else:
    print('Esto se terminó')

#List comprehension, lsita de compresion
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
#compresion o tomar lo necesario, creando una lista nueva
# p para cada elemento en singular.. con el for recorremos todos los elementos con la condicion P
alongP = [p for p in names if p[0] == "P"] #Esto filtra lo que queremos sin modificar la lista
print(alongP)

#diccionario
bottleC = [{"name": "Quilmes","country": "Arg"},
           {"name": "Corona","country": "Mx"},
           {"name": "Stella Artrois","country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg) #vemos la extracion
print(bottleC) #veo todo el diccionario

#Paso de Argumentos (funciones)
def mi_funcion2(name, lastName): #en la funcion dentro los parantesis hay parametros
    print("Saludos a todos los que ven a través del canal de you tube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2('Jorge', 'Lucero') #los argumentos son necesarios, son el valor que va a recibir
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78 , 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")#f se llama interpolación

#def sumar2(a int= 0, b int= 0): poner int es redundante
def sumar2(a = 0, b = 0): #le damos un valor por default
    return a + b
resultado = sumar2() #no le paso nada entonces debo dar un valor x default
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar2(22, 66)}") #al pasar un argumento valido lo toma
# al tomar el valor valido cambia el valor default

#Argumentos variables en funciones
def listasNombres(*nombres): #*nombres ya que no los conocemos,
    # normalmente se usa *args, no conozco la cantidad
    for nombre in nombres: # se convierte en una tupla que no puede ser modificada
        print(nombre)
listasNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'María')
listasNombres('Marcos', 'Daniel', 'Romina', 'Marcela', 'Carlos') #cada vez que
# llamo a la función se le agregan y muestran todos

# Diccionario
def listarTerminos(**terminos): # Lo mas utilizado es **kwargs (no **terminos)
    #kwargs es llave valor argumentos, (Diccionarios)
    #si quiero agrandar, pasar varios parametros, debo poner dentro de los parantesis
    # ej (nombre, **nombres, **terminos)  nombre->argumetos fijos,
    # *nombres->lista argumento variables,
    # y **terminos-> tupla para diccionario
    # para recibir los argumentos (llave palabras argumentos)
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # No recibe nada, nada se va a mostrar, debo pasar argumentos
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primary Key')
#las llaves no llevan comillas y reciben cualquier valor
listarTerminos(Nombre='Leonel Messi') #en la llave no puedo poner 10 solo string

#lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla') #es una cadena y la muestra vertical, para
# que no sea así debo hacer una variable nueva
# desplegarNombres(10, 11) # No es un objeto iterable xq es entro
desplegarNombres((10, 11)) # La convertimos a una tupla con doble (()), en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista ([])


# Funciones Recursivas, necesita un caso base y uno recursivo
def factorial(numero): #(parámetro número)
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo


resultado = factorial(5) # Lo hacemos en código duro
print(f'El factorial del número 5 es: {resultado}')
# Tarea que el usuario ingrese el número para calcular el factorial
5
numeroFactorial = int(input('Digite el numero para calcular el factorial: '))
resultado = factorial(numeroFactorial)
print(f'El factorial del número {numeroFactorial} es: {resultado}')


