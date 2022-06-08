'''
Clase 7 ejercicio 4
Que el usuario ingrese su edad
y segun su etapa de vida imprima una breve oracion
0 a 10 = La infancia es incríble y Bella
10 a 19 = Tienes muchos cambios, mucho que estudiar
20 a 29 = Amor y comienza el trabajo
... completar las siguientes etapas
'''

edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10:
    mensaje = 'La infancia es increíble y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Que nada detanga tus sueños'
elif 40 <= edad < 50:
    mensaje = 'como un buen vino... mejoras con los años'
elif 50 <= edad < 60:
    mensaje = 'que la edad es una barrera solo cuando tu mente decide que asi sea'
elif 60 <= edad < 70:
    mensaje = 'Eres el amo de tu destino'
elif 70 <= edad < 80:
    mensaje = 'Disfruta de las pequeñas cosas'
elif 80 <= edad < 90:
    mensaje = 'has que cada dia cuente'
elif 90 <= edad < 100:
    mensaje = 'dias de regalo, disfrutalos'
elif 100 <= edad <110:
    mensaje = 'eres increible'
else:
    mensaje = 'has superado toda expectativa de vida'
print(f'Tus {edad} años {mensaje}')
