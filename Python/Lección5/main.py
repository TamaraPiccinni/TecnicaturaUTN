#Comenzamos con funciones

#mi_funcion() no se puede llamar antes de definirla

#Definimos una función
# con snake_casse para practicar. los () son necesarios

def mi_funcion(): #para identificar esta funcion usamos ()
    print('Feliz dia del programador')

mi_funcion()  #llamamos la funcion
mi_funcion() #se puede llamar N cantidad de veces

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+ ' '+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1]) #pasamos uno por uno los datos de la lista a la funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Osvaldo", "Giordanini") #desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"} #diccionario
show(**person3) #** usamos dos porque recorre 2 elementos

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
mi_funcion2('Jorge', 'Lucero')
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones
# Creamos uina función para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78 , 22)
#print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a = 0, b = 0): #le damos un valor por default
    return a + b
resultado = sumar2()
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar2(22, 66)}") #al pasar un argumento valido lo toma

#Argumentos variebles en funciones
def listasNombres(*nombres): #*nombres ya que no los conocemos, normalemente se usa *args
    for nombre in nombres: # se convierte en una tupla que puede ser modificada
        print(nombre)
listasNombres('Lucas', 'Jose', 'Claudia', 'Rosa', 'María')
listasNombres('Marcos', 'Daniel', 'Romina', 'Marcela', 'Carlos') #cada vez que llamo a la funcion se le agregan


