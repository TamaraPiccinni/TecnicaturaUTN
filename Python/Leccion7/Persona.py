class Persona: #Esta case hereda de la clase objet
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # override =sobreescribir
        return f'Persona: [ Nombre: {self.nombre}, Edad: {self.edad} ]'

class Empleado(Persona): #Esta es la clase hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [ Sueldo: {self.sueldo} ] {super().__str__()}' #super sobreescribo llamando a srt de pernsona





empleado1 = Empleado('Ariel', 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapsular los atributos y agregar los metodos getters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

