import psycopg2 # Esto es para poder conenctarnos a Postgre
# objeto de tipo conexion
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
# print(conexion)

cursor = conexion.cursor()  # con el objeto cursor puedo ejecutar sentencias
sentencia = 'SELECT * FROM persona' # esto es una cadena para la variable sentencia
cursor.execute(sentencia) # de esta manera ejecutamos la sentencia
registros = cursor.fetchall() # recupera todos los registros de esta sentencia que serán una lista,
# aunque internamente tenemos 2 tuplas (envueltas en una lista

print(registros)

# cerrar los objetos que se conectaron a la base de datos
cursor.close()
conexion.close()