#Ejercicio 10: No repetir caracteres
# Hacer un programa que pida una cadena por teclado, luego
#meter los caracteres en una lista sin repetir caracteres

cadena = input("Digite una frase: ")
lista = []
for i in cadena:
    if i not in lista: #si el caracter no esta en la lista
        lista.append(i) #lo agregamos a la lista
print(f"\nLista de caracter sin repetir ninguno: \n {lista}")