
archivo = open('prueba.txt', 'r', encoding='utf8')
# cambio la r (read) leer por:
# w (write) para escribir info o crea el archivo si no existe, si ya tiene info la borra
# a (append) anexa información a un archivo que ya tiene info
# x para crear, pero si no existe regresa error
#  print(archivo.read())
# print(archivo.read(16))
# print(archivo.read(10))  # continuamos desde la linea anterior
# print(archivo.readline())
# print(archivo.readline()) # continua en la siguiente linea

# Vamos a iterar el archivo en cada una de las líneas
# for linea in archivo:
    # print(linea) # Iteramos todos los elementos del archivo
# print(archivo.readlines()[11]) # accedemos al archivo como si fuera una lista,
# por eso accedemos con corchetes

# Anexamos información, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8') # si uso a en vez de w se copia cada vez que ejecute
archivo2.write(archivo.read())
archivo.close() # cerramos el primer archivo
archivo2.close() # cerramos el segundo archivo

print(' Se ha terminado el proceso de leer y copiar archivos')