"""
Clase 9
Ejercicio 4
Con un conjunto de calificaciones de 10 alumno.
Calcular la calificacion promedio y la calificacion mas baja de todo el grupo
"""
'''
suma = 0
calificacionBaja = 999

for i in range(0,10):
    calificacion = float(input("Digite una calificacion: "))
    suma += calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
promedio= suma/10
print(f"\nLa calificacion promedio es: {promedio}"
      f"\nLa calificacion mas baja es: {calificacionBaja}")'''
'''
