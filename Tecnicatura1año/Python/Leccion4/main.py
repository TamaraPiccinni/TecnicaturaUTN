#Caracteristicas fundamentales de un programador
#buscar soluciones
#Reparar errores
#Crear proyectos
'''
Las Tuplas son inmutables, mientras que las Listas son mutables.
Las tuplas en Python son inmutables, lo que significa que una vez creada una tupla,
sus elementos no pueden cambiar. Las tuplas no pueden ser alteradas
'''
#Colecciones en Python
#las Listas en otros lenguajes se lo conoce como arreglos o vectores
print("")
print('Lista, se puede modificar')
# lista = Ariel , Liliana, Natalia, Osvaldo
# indices   0       1       2         3
print("")
nombres = [ 'Naty0', 'Osvaldo1', 'Lily2', 'Ariel3'] #elementos de la lista
print(nombres) # muestra la lista completa
print("")
print(nombres[0]) #muetra la posición 0
print(nombres[1])
print(nombres[3])
print("")
print(nombres[-1]) # muestra el último
print(nombres[-2])
print("")

print(nombres[0:2]) #solo muestra el indice 0, 1 pero no el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) # muestra 0, 1, 2
#Desde el índice indicado hasta el final
print(nombres[1: ])
#modificamos un valor
nombres[2] = 'Liliana2'
nombres[0] = 'Natalia0'
print(nombres)
print("")

#iterar una lista
for nombre in nombres: #nombre es singular(puedo usar cualquier variable, la lista nombres es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')
print("")
# Preguntamos cuantos elementos tiene
print(f"La lista nombres tiene: {len(nombres)} elementos") #le pasamos como parámetro la lita
print("")

#agregamos un elemento, puede tener diferentes tipos de datos
nombres.append('Marcelo4') # se ingresa al final
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)
print(nombres)
print("")
#insertamos un elemento en un índice específico
nombres.insert(1, 'Alberto1') #no olvidar el entero del índice (donde va)
print(nombres)
print("")
nombres.insert(3, 'Debora3')
print(nombres)
print("")
#eliminamos un elemento
nombres.remove('Alberto1')
print(nombres)
print("")

#eliminar el último elemento (el último en la posición final)
nombres.pop()
print(nombres)
print("")

#eliminar un indice especifico
del nombres[2] #del significa delete (eliminar)
print(nombres)
print("")

#eliminar, borrar o limpiar todos los elementos
nombres.clear()
print(nombres)
print("")

#eliminar la lista
del nombres
#print(nombres) #da error xq lo eliminé usando del por eso no la muestra
print("")

#Definimos una tupla entre ()
print('Tupla: inmutable')
print("")
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))
print("")

#Acceder a un elemento, para esto usamos [] no ()
print(cocina[0])

#mostrar de manera inversa
print(cocina[-1])
print("")

#acceder a un rango
print(cocina[0:1]) #muestra solo el 0 xq siempre muestra uno menos, no muestra el ultimo
print(cocina[0:2])
#ejemplo
#verderuas = ('papa') #esto es una string, cadena porque no tiene la coma
verduras = ('papa', ) #este si es tiene un elemento y una coma
print("")

#Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #agrego end para que print deje de usar \n para saltos de linea y se vea en una lienea
print("")
'''
cocina[0] = 'plato'
print(cocina) #da error xq no se puede o debe modificar
'''

#si hace falta modificarla (no es lo ideal, no es una buena practica, lo convertimos en lista
cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)
print("")

#eliminamos
#del cocina
# para eliminar una tupla

#Lista mantiene un orden se puede modificar es mutable
#tupla mantiene un orden NO se puede modificar es inmutable
#Coleccion del tipo (SET) C no tiene orden, no puede almacenar elementos repetidos, No se puede modificar,
#pero puede agregar o eliminar. Impresión es aleatoria

#Tipo set o conjuntos uso {}
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print("")
print(len(planetas)) #len = largo
print("")

#revisamos si un elemento existe dentro del elemento, tipo booleano
print('Marte' in planetas)
print('Jupiter' not in planetas)
print("")

#Agregar un elemento
planetas.add('Tierra') #add es una función, no puedo agregar lo mismo xq da error
print(planetas)
print("")

#Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') #si ingresamos con un error o no existe da error
print(planetas)
print("")

planetas.discard('tierra') #no da error pero tampoco borra (escribo con minuscula es un error)
print(planetas)
print("")

planetas.discard('Tierra')
print(planetas)
print('')

#Limpiar set o conjunto
planetas.clear()
print(planetas)
print("")

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

#vemos el largo o cantidad de elementos
print(len(diccionario))
print(diccionario)
print("")

#Acceder a un diccionario con la llave (key), se debe escribir sin errores
print(diccionario['IDE'])
print("")

#otra forma de recuperar (ver) una llave
print(diccionario.get('POO')) #get = obtener
print(diccionario.get('SABD'))
print("")

#Modificar los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)
print("")

#Como recorrer los elementos
for termino in diccionario:
    print(termino)
print("")

#asi da error necesitamos una funcion
#for termino, valor in diccionario:
#    print(termino, valor)

for termino, valor in diccionario.items():
    print(termino, valor)
print("")

#Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): #estamos usando una funcion
    print(termino) #muestra solo las llaves
print("")

for valor in diccionario.values(): #Estamos usando una funcion para acceder
    # al valor sin las llaves
    print(valor)
print("")

#comprobamos la existencia de algun elemento
print('IDE' in diccionario) #devuelve valor booleano
print("")

#Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)
print("")

#Elimanos un elemento
diccionario.pop('SABD')
print(diccionario)
print("")

#vaciar un diccionario
diccionario.clear()
print(diccionario)
print("")

#Eliminar diccionario
del diccionario #el diccionario de borro
#print(diccionario) #da error xq ya no esta

#concatenar Listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2 # Concatenamos
print(lista3)
print("")

#para agregar varios elementos en la lista
lista3.extend([7, 8, 9, 1]) # función para agregar varios elementos
print(lista3)
print("")

#para ver en que lugar esta el elemento
print(lista3.index(5))
#print(lista3.index(0)) #da error si un elemento no esta
print("")

#para ver cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))
print("")

#Poner la lista descendente o ascendente, al reves
lista3.reverse()
print(lista3)
print("")

#Para que una lista se multiplique repitiendo sus elementos
lista3 = [1, 2, 3] * 2
print(lista3)
print("")

#Metodos de ordenamiento
lista3.sort() #los ordea ascendente
print(lista3)
print("")
lista3.sort(reverse=True) #descendente
print(lista3)
print("")

#repaso Tupla puede tener diferentes de tipos de datos dentro
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)
print("")

#puedo convertir la lista en tupla y viceversa
#puedo usar funciones len, index, count
print(4 in tupla) # buscar un elemento, booleana. puedo preguntar si esta o no esta con not
print("")

#Repaso de set o conjunto
#para definir un conjunto
conjunto2 =set() #este se puede inicializar vacio
conjunto1 = {'bye',} #con llaves debe tener contenido
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print("")
print(conjunto1)
print(3 not in conjunto1) #preguntamos si el número 3 está en el conjunto1
print("")

#como hacer la igualdad en dos conjuntos
print(conjunto1 == conjunto2) #nos devuelve una respuesta Booleana
print("")

#operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 #la linea | une dos conjuntos
print(conjunto3)
print("")

conjunto3 = conjunto1 & conjunto2 #Que elemento tiene en comun
print(conjunto3)
print("")

conjunto3 = conjunto1 - conjunto2 #asigna el valero que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
print("")

conjunto3 = conjunto2 - conjunto1 #inversa
print(conjunto3)
print("")

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten, diferentes entre ambos
print(conjunto3)
print("")

#determinar si un conjunto es sub conjunto de otro (si esta dentro de otro)
conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) #preguntamos si es un cubconjunto
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))
print("")

#comprobamos si son disconexo, no comparten ningun elemento en comun
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))
print(conjunto1.issuperset(conjunto3))
print("")

#si ambos son disconexos
print(conjunto1.isdisjoint(conjunto2)) #no hay cosas en comun
print("")

#convertir un conjunto totalmente inmutable
conjunto1 = frozenset #esto hace que el conjunto sea totalmente inmutable
#no se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso Diccionarios
diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)
print("")

#como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)
print("")

#los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad' :40,'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia' :[35, 1.67]}
# almacena diferentes tipos de datos, colecciones
#cadena, diccionario y lista (tipo entero, flotante)
print(diccionario2)
print("")

seleccionArgentina = {
    10: {'Nombre' : 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre' : 'Angel Di María', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    21: {'Nombre' : 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre' : 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa centrañ'},
    1: {'Nombre' : 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
}
print(seleccionArgentina)
print(seleccionArgentina[10]) #solo muestra a messi
print(seleccionArgentina.values()) #solo los datos
print("")

#print mas ordenado manera comun
for llave in seleccionArgentina:
    print(llave)\

#usando la variable para ver solo el valor
for valor in seleccionArgentina.values():
    print(valor)

#para ver todos los datos
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("")

#Como tarea agregar 4 jugadores mas al diccionario seleccionArgentina
print('Tenemos cargados en el diccionario: ', end=' ')
print(len(seleccionArgentina))
print("")

seleccionArgentina[23] = {'Nombre' : 'Emiliano Martinez', 'Edad': 29, 'Altura': 1.96, 'Precio': '28 Millones', 'Posicion': 'Portero'}
seleccionArgentina[6] = {'Nombre' : 'German Pezzella', 'Edad': 31, 'Altura': 1.83, 'Precio': '5 Millones', 'Posicion': 'Defensa Central'},
seleccionArgentina[14] = {'Nombre' : 'Exequiel Palacios', 'Edad': 23, 'Altura': 1.78, 'Precio': '22 Millones', 'Posicion': 'Centrocampista'},
seleccionArgentina[20] = {'Nombre' : 'Giovani Lo Celso', 'Edad': 26, 'Altura': 1.78, 'Precio': '22 Millones', 'Posicion': 'Centrocampista'},
print(seleccionArgentina)
print("")

#Metodo de trabajos 'Pilas' (es un tipo de listas)
#Pilas usando listas (la pila se agrega o elimina x el final)
pila = [1, 2, 3]

#agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)
print("")

#Sacamos elementos por el final
elementoBorrado = pila.pop() #quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila quedo así: {pila}')
print("")

#Colas con Listas (Colas es otro tipo de listas)
#Estructura de datos tipo fifo (first input /first output)
#primero en entrar será el primero en salir
#python suele usar esto con el modo collection, pero vamos a hacerlo manual
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
cola.append('Natalia')
cola.append('Jose')
print(cola)
print("")

#Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
print("")

#mostramos como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i}-> {seleccionArgentina[i]}')
print("")

