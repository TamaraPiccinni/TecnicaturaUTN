#Caracteristicas fundamentales de un programador
#buscar soluciones
#Reparar errores
#Crear proyectos

# lista = Ariel , Liliana, Natalia, Osvaldo
# indices   0       1       2         3

nombres = [ 'Naty0', 'Osvaldo1', 'Lily2', 'Ariel3']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) #solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) # muestra 0, 1, 2
#Desde el indice indicado hasta el final
print(nombres[1: ])
#modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
#iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
# Preguntamos cunatos elementos tiene
print(len(nombres)) #le pasamos como parametro la lita

#agregamos un elemento
nombres.append('Marcelo4')
print(nombres)

#insertamos un elemento en un indice especifico
nombres.insert(1, 'Alberto1') #no olvidar el entero del indice
print(nombres)
nombres.insert(3, 'Debora3')
print(nombres)

#eliminamos un elemento
nombres.remove('Alberto1')
print(nombres)

#eliminar el ultimo elemento
nombres.pop()
print(nombres)

#eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)

#eliminar la lista
del nombres
#print(nombres) #da error xq lo elimine la linea 56

#Definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

#Acceder a un elemento, para esto usamos [] no ()
print(cocina[0])

#mostrar de manera inversa
print(cocina[-1])

#acceder a un rango
print(cocina[0:1]) #muestra solo el 0 xq siempre muestra uno menos, no muestra el ultimo
print(cocina[0:2])
#ejemplo
#verderuas = ('papa') #esto es una strin, cadena porque no tiene la coma
verduras = ('papa', ) #este si es tiene un elemento y una coma

#Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #agrego end para que deje de usar \n para saltos de linea y se vea en una lienea
'''
cocina[0] = 'plato'
print(cocina) #da error xq no de puede, debe modificar
'''

#si hace falta modificarla (no es lo ideal, no es una buena practica, lo convertimos en lista
cocinaLista = list(cocina)
cocinaLista[0] = 'Palto'
cocina = tuple(cocinaLista)
print('\n', cocina)

#eliminamos
#del cocina
# para eliminar una tupla

#Lista mantiene un orden se puede modificar es mutable
#tupla mantiene un orden NO se puede modificar es inmutable
#Coleccion del tipo C no tiene oreden, no puede almacenar elementos repetidos, No se puede modificar,
#pero puede agregar o eliminar. impresion es aleatoria

#Tipo set o conjuntos
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas)) #len = largo

#revisamos si un elemento existe dentro del elmento, tipo booleano
print('Marte' in planetas)
print('Jupiter' not in planetas)

#agregar un elemento
planetas.add('Tierra') #add es una función
print(planetas)

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') #si ingresamos con un error o no existe da error
print(planetas)

planetas.discard('tierra') #no da error pero tampoco borra
print(planetas)

#Limpiar set o conjunto
planetas.clear()
print(planetas)

#eliminar set o conjunto
del planetas
#print(planetas) # al eliminar nos muestra un error (por eso lo comentamos)

#diccionarios, esta compuesto por dos elementos
# 'Maradona' : 10
#  cadena     elemento
# UNA LLAVE Y UN VALOR
# dic(key, value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programacion Orientada a objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
    }
print(diccionario)


#Repaso de ser o conjunto
#para definir un conjunto
conjunto2 =set() #este se puede inicializar vacio
conjunto1 = {'bye',} #con llaves debe tener contenido
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el nuemro 3 esta en el conjunto1

#como hacer la igualdad en dos conjuntos
print(conjunto1 == conjunto2) #nos devuelve una respuesta Booleana

#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #la linea | une dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #Que elemento tiene en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #asigna el valero que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1 #inversa
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten, diferentes entre ambos
print(conjunto3)

#determinar si un conjunto es sub conjunto de otro (si esta dentro de otro)
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #preguntamos si es un cubconjunto
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

#comprobamos si son disconexo, no comparten ningun elemento en comun
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))
print(conjunto1.issuperset(conjunto3))

#si ambos son disconexos
print(conjunto1.isdisjoint(conjunto2)) #no hay cosas en comun

#convertir un conjunto totalmente inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
#no se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
#como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad' :40,'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia' :[35, 1.67]}
# almacena diferentes tipos de datos, colecciones
#cadena, diccionario y lista (tipo entero, flotante)
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre' : 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre' : 'Angel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre' : 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre' : 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa centrañ'},
    1: {'Nombre' : 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
}
print(seleccionArgentina)
print(seleccionArgentina[10]) #solo muetra a messi
print(seleccionArgentina.values()) #solo los datos

#print mas ordenado manera comun
for llave in seleccionArgentina:
    print(llave)\

#usando la variable para ver solo el valor
for valor in seleccionArgentina.values():
    print(valor)

#para ver todos los datos
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#Como tarea agregar 4 jugadores mas al diccionario seleccionArgentina
print('Tenemos cargados en el diccionario: ', end=' ')
print(len(seleccionArgentina))

#23: {'Nombre' : 'Emiliano Martinez', 'Edad': 29, 'Altura': 1.96, 'Precio': '28 Millones', 'Posicion': 'Portero'},
#6: {'Nombre' : 'German Pezzella', 'Edad': 31, 'Altura': 1.83, 'Precio': '5 Millones', 'Posicion': 'Defensa Central'},
#14: {'Nombre' : 'Exequiel Palacios', 'Edad': 23, 'Altura': 1.78, 'Precio': '22 Millones', 'Posicion': 'Centrocampista'},
#20: {'Nombre' : 'Giovani Lo Celso', 'Edad': 26, 'Altura': 1.78, 'Precio': '22 Millones', 'Posicion': 'Centrocampista'},

#Metodo de trabajos 'Pilas'
#Pilas usando listas
pila = [1, 2, 3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos por el final
elementoBorrado = pila.pop() #quita el ultimo elemnto y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pilaquedo así: {pila}')

#Colas con Listas
#Estructura de datos tipo fifo (first input /first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
cola.append('Natalia')
cola.append('Jose')
print(cola)

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
