'''
Clase 9
Calcular la suma de 'N' primeros numeros
'''

num = int(input("Digite la cantidad de numeros a sumarse: "))
suma = 0

for i in range(1, num+1):
    suma += i
print(f"La suma es: {suma}")

