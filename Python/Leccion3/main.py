# Ciclo While (mientras o durante)

'''
#Este es un ciclo infinito

condicion = True
while condicion: #respetar identacion, tabulacion, eso determina lo que es parte del ciclo
    print('Ejecutando nuestro ciclo while')
else:
    print('Fin del ciclo while')
'''
'''
contador = 0
while contador < 78:
    print('Ejecutamos nuestro ciclo while',contador) # puedo usar la interpolacion f, la mas usada. (f de format)
    contador += 1 #si no lo incremento seria infinito (xq seguiria en 0)
else:
    print('fin del ciclo while')'''

'''
#imrpimir números del 0 al 5 con el ciclo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1 #si no lo incremento seria infinito (xq seguiria en 0)
'''
'''
#imrpimir números del 5 al 1 con el ciclo while
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1
'''
'''
#Ciclo for (para hasta con paso hacer) numero determinado de iteraciones
# vamos a iterar una cadena, es decir un arreglo de caracteres.ç
# iterar es recorrer un ciclo
cadena = 'Hello'
for letra in cadena: #in es indice
    print(letra)
else:
    print('Fin del ciclo for')
# en otros leguajes se lo conoce como for each (por cada elemento)
'''
'''
#Palabra reservada break
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break #al agregar brake hace un corte (rompe el ciclo) cuando encuentra la primera
else: #con el break ni siquiera llega al else cuando encuetra lo que busca
    print('Fin del ciclo for')
'''
'''
# Palabra reservada continue
for i in range(6): #funcion de rango (lo hace de 0 a 5) por eso muestra del 0, 4 y 6
    if i % 2 == 0:
        print(f'Valor : {i}')

for i in range(6):
    if i % 2 != 0: #diferente es decir impares en este caso
        continue #es omitir eludir todos los numeros que sean impares
        print(f'Valor : {i}') '''
