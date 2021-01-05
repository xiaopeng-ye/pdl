class GestorError:

    def __init__(self):
        self._error_file = open('../error.txt', 'w', encoding='UTF-8')
        self.error_lexico = {'_': 'No es válido empezar con _ en un identificador',
                             "'": 'Cadena de texto inválido',
                             }

    def imprime(self, analizador, mensaje, linea):
        self._error_file.write(f'Error {analizador}: {mensaje} en la línea {linea}')
        self._error_file.close()
        raise Exception(f'Error {analizador}: {mensaje} en la línea {linea}')
