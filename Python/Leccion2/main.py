# En esta clase veremos la sentecncia if/else
'''
condicion = True #pruebo cambiar valores falso o 10 o 0
if condicion:
    print("condicion Verdadera")
else:
    print('condicion falsa')

condicion = 0 # pongo el punto de ruptura para observar el debug (depuerar) se suele poner en una variable
if condicion ==  True:
    print("condicion Verdadera")
elif condicion == False:
    print('condicion falsa')
else:
    print("condicion sin especificar")

condicion ='hola alumnos' # al ser una cadena y no un dato bool da sin especificar
if  condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print("condicion sin especificar")


# conversion de numero a texto
num = int(input("Digite un numero en el rango del 1 al 3: "))
numTexto = ''
if num == 1:
   numTexto = 'Número uno'
elif num == 2:
    numTexto = 'Número dos'
elif num == 3:
    numTexto = 'Numero tres'
else:
    numTexto= 'Has ingresado un numero fuera de rando'
print(f'El número ingresado es: {num} - {numTexto} ') #no debe haber ningun espacio para que no lo tome como la estructura
#si dejamos un espacio o tab lo tomo como parte de la estructura da error y no muestra el resultado
'''

#operador ternario (remplaso las 4 lineas de codigo en una)

condicion = True
# if condicion:
#     print("condicion Verdadera")
# else:
#     print('condicion falsa')

#esto solo se recomienda en bloques simplificado, si tiene mas lineas no se recomienda
print('condicion verdadera') if condicion else print('condicion falsa')
