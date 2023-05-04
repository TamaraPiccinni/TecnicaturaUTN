from ManejoArchivos import ManejoArchivos

# MANEJO DE CONTEXTO WITH: Sintaxis simplificada, abre y cierra el archivo
# si no lo abro y cierro python lo hace automático, pero es una buena práctica hacerlo

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
#    print(archivo.read())

# No hace falta ni el try, ni el finally
# en el contexto de with lo qye se ejecuta de manera automática
# Utiliza diferentes métodos: __enter__ este es que abre
# Ahora el siguiente método es que cierra: __exit__

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
