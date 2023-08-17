from capa_datos_persona.usuario_dao import UsuarioDAO
from logger_base import log

opcion = None
while opcion != 5:
    print('Opciones:')
    print('1. Listar usuario')
    print('2. Agregar usuario')
    print('3. Modificar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Escribe tu opcion (1-5): '))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input('Escribe el nombre de usuario: ')
        password_var = input('Escribe la contraseña: ')
        usuario = UsuarioDAO(username=username_var, password=password_var)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion == 3:
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nombre de usuario a modificar: ')
        password_var = input('Escribe la contraseñaa modificar: ')
        usuario = UsuarioDAO(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_actualizado}')
    elif opcion == 4:
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = UsuarioDAO(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuario eliminado: {usuario_eliminado}')

else:
    log.info('Salimos de la aplicación, Hasta pronto!!')
