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
print(nombres) #da error xq lo elimine la linea 56
