from collections import OrderedDict


class GestorTablaSimbolo:
    def __init__(self):
        self._lista_ts = []
        self._global = TablaSimbolo('global')
        self._lista_ts.append(self._global)
        self._actual = self._global
        self._zona_decl = False

    def crea_tabla(self, nombre_funcion):
        self._actual = TablaSimbolo(nombre_funcion)
        self._lista_ts.append(self._actual)

    def busca_ts(self, lexema):
        return self._actual.posicion_lexema(lexema)

    def buscar_ts_activa(self, lexema):
        return self._actual.posicion_lexema(lexema)

    def inserta_ts(self, lexema):
        return self._actual.insertar_lexema(lexema)

    def imprime_fichero(self):
        with open('tabla_simbolos.txt', 'w') as f:
            for i, tabla in zip(range(1, len(self._lista_ts) + 1), self._lista_ts):
                f.write(f"TABLA {tabla.nombre} # {i} :\n")
                f.write(str(tabla))
                f.write('-------------------------------------')


class TablaSimbolo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._simbolos_dict = OrderedDict()
        self._simbolos_list = []
        self._despl = 0

    @property
    def nombre(self):
        return self._nombre

    def insertar_lexema(self, lexema):
        simbolo = Simbolo(lexema)
        self._simbolos_dict[lexema] = simbolo
        self._simbolos_list.append(simbolo)
        return len(self._simbolos_list) - 1

    def posicion_lexema(self, lexema):
        if lexema in self._simbolos_dict:
            return list(self._simbolos_dict).index(lexema)
        else:
            return None

    def get_lexema(self, indice):
        return self._simbolos_list[indice]

    def __str__(self):
        return ''.join([str(simbolo) for simbolo in self._simbolos_dict.values()])


class Simbolo:
    def __init__(self, lexema):
        self._lexema = lexema
        self._propiedad = {}

    def __setitem__(self, key, value):
        self._propiedad[key] = value

    def __getitem__(self, key):
        return self._propiedad[key]

    def __str__(self):
        return f"* LEXEMA : '{self._lexema}'\n  ATRIBUTOS :\n" + '\n'.join(
            [u"  + {key} : {value}".format(key=key, value=("'" + value + "'") if isinstance(value, str) else value) for
             key, value in self._propiedad.items()])


if __name__ == '__main__':
    ts = TablaSimbolo('Global')
    ts.insertar_lexema('factorial')
    s = ts.get_lexema(0)
    s['tipo'] = 'funcion'
    s['numParm'] = 2
    s['tipoParam1'] = 'boolean'
    s['tipoParam2'] = 'string'
    ts.insertar_lexema('var2')
    s = ts.get_lexema(1)
    s['tipo'] = 'entero'
    s['despl'] = 8
    print(ts)
