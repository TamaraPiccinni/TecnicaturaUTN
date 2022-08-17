'''
Clase 7
ejercicio 5
sistemas de calificaciones
le pedimos al usuario que ingrese un valor del 0 al 10

si ingreso
9 o 10 imprimimos A
entre 8 y 9 B
7 8 C

'''
'''
puntaje = float(input('Digite el puntaje del 0 al 10: '))
mensaje = None
if 9 <= puntaje <= 10:
    mensaje = 'A'
elif 8 <= puntaje < 9:
    mensaje = 'B'
elif 7 <= puntaje < 8:
    mensaje = 'C'
elif 6 <= puntaje < 7:
    mensaje = 'D'
elif 0 <= puntaje < 6:
    mensaje = 'F'
else:
    mensaje = 'Valor incorrecto'
print(f'La calificacion correspondiente es: {mensaje} ')

'''
#opcion del profe
puntaje = int(input('Digite el puntaje del 0 al 10: '))
mensaje = None
if 9 <= puntaje <= 10:
    print('A')
elif 8 <= puntaje < 9:
    print('B')
elif 7 <= puntaje < 8:
    print('C')
elif 6 <= puntaje < 7:
    print('D')
elif 0 <= puntaje < 6:
    print('F')
else:
    print('Valor incorrecto')

