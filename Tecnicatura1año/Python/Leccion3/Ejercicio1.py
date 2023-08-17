'''
Clase 9
Diseñar un programa que ingresando un año, nos devuelva, si es bisiesto o no,
repetir hasta que el usuario lo desida"
'''

año = int(input("Digite un año para comprobar si es bisiesto o 0 para terminar: "))

while año != 0:

    if(año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print(f"El año {año} es Bisiesto")
        año = int(input("Digite un año para comprobar si es bisiesto o 0 para terminar: "))
    else:
        print(f"El año {año} NO es Bisiesto")
        año = int(input("Digite un año para comprobar si es bisiesto o 0 para terminar: "))

