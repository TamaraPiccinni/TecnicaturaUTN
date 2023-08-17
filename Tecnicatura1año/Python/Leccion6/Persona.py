class Persona: #Creamos una clase
   #pass #no se procesa nada más (No tiene contenido)

#print(type(Persona))
#el método init es el método especial de inicialización para los atributos
# vamos a trabajar con argumentos variables (tuplas y diccionarios) ej *args
# el primero es para tuplas (*args), y el segundo es para el diccionario variable (**kwargs)
       def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama método Init Dunder
           self.nombre = nombre #atributos del metodo no de la clase
           self.apellido = apellido
           self._dni = dni #Este atributo esta encapsulado de manera sugeriada
           self.edad = edad
           self.args = args
           self.kwargs = kwargs

       def mostrar_detalle(self):
           #ahora que agregue *args y **kwargs modifico la salida
           #print(f'Persona: {self.nombre} {self.apellido} {self.edad}') asi era antes
           print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 32456987, 40)  # Necesitamos enviar argumentos
# print(persona1.nombre) # Tarea: Hacer el print igual que con el objeto 2
# print(persona1.apellido)
# print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')
persona2 = Persona('Osvaldo', 'Giordanini', 30321456, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

# Los atributos son: caracteristicas
# Los métodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dara error
persona1.telefono = '03456' #atributo superficial, xq solo persona1 puede usarlo
print(f'Este es el telefono de {persona1.nombre}: {persona1.telefono}') #hemos creado un atributo de uno bjeto

#si quiero acceder desde persona2 da error
# print(persona2.telefono) el objeto persona2 no tiene este atributo
persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Telélefono', 351555555, 'Calle Lopez', 823, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni) esto no se debe utilizar (esta encapsulado), esto dice que desconocemos el lenguaje
#persona3.__nombre #así (__) esta totalmente encapsulado



