from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:
    '''
    DAO -> Data Access Object para la tabla usuario
    CRUD -> Create, Read, Update, Delete
    '''

    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando los usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    #Eliminar un usuario:
    usuario = Usuario(id_usuario=3)
    usuarios_eliminados = UsuarioDAO.eliminar(usuario)
    log.debug(f'Usuarios eliminados: {usuarios_eliminados}')

    #Actualizar un usuario:
    usuario = Usuario(id_usuario=1, username='', password='369')
    usuarios_modificado = UsuarioDAO.actualizar(usuario)
    log.debug(f'Usuarios modificado: {usuarios_modificado}')

    #Insertar un usuario:
    usuario = Usuario(username='Juan', password='123')
    usuarios_insertados = UsuarioDAO.insertar(usuario)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

    #Listar o seleccionar todos los registros:
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)