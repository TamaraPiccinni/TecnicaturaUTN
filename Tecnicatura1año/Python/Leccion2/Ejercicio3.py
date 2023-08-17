'''
clase 7
Ejercicio 3
Calcular la estacion del año
Pedir al usuario que ingrese un mes del año, el valor debe ser entre 1 y 12,
y le decimos en que estacion esta
#aqui utilizo None que indica que la variable no tiene un valor asignado
#None es == a null otros lenguajes como Java
'''

mes = int(input('Digite un mes del año (de 1 al 12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:'Ese mes no existe'
print(f'La estacion es: {estacion}, para el mes seleccionado: {mes}')
