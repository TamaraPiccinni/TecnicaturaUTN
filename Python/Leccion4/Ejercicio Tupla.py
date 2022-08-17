'''
#Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la tupla
crear una lista que solo incluya los nuemero menores a 5
e imprimirla por consola [1, 3, 2]
'''

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = [] #Definimos la lista
#filtramos los menores a 5
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)