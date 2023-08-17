class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '_'))
        self.nombre = open(self.nombre, 'r', encoding='utf8') # Encapsulamos el código
        # dentro del método
        return self.nombre

    def __exit__(self, tipo_exception, val_eception, traza_error): # por dafault exc_type, exc_val, exc_tb
        print('cerramos el recurso'.center(50, '_'))
        if self.nombre:
            self.nombre.close() # cerramos el archivo