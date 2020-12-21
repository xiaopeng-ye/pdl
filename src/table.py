from collections import OrderedDict


class GestorTablaSimbolo:
    def __init__(self):
        self.lista_ts = []
        self.global_ = TablaSimbolo('global')
        self.lista_ts.append(self.global_)
        self.actual = self.global_
        self.zona_decl = False

    def crea_tabla(self, indice):
        self.actual = TablaSimbolo(self.global_.get_simbolo(indice).lexema)

    def libera_tabla(self):
        self.lista_ts.append(self.actual)
        self.actual = self.global_

    def busca_ts(self, lexema):
        index = self.actual.posicion_lexema(lexema)
        return index if index else self.global_.posicion_lexema(lexema)

    def busca_ts_activa(self, lexema):
        return self.actual.posicion_lexema(lexema)

    def inserta_ts(self, lexema):
        return self.actual.insertar_lexema(lexema)

    def aniadir_variable_ts(self, indice, tipo, tam):
        simbolo = self.actual.get_simbolo(indice)
        simbolo['tipo'] = tipo
        simbolo['despl'] = self.actual.despl
        self.actual.despl += tam

    def aniadir_funcion_ts(self, indice, numParam, tipoParam, tipoRetorno):
        simbolo = self.actual.get_simbolo(indice)
        simbolo['tipo'] = 'funcion'
        simbolo['numParam'] = numParam
        simbolo['tipoParam'] = tipoParam
        simbolo['tipoRetorno'] = tipoRetorno
        simbolo['etiquta'] = simbolo.lexema

    def buscar_simbolo_ts(self, indice):
        simbolo = self.actual.get_simbolo(indice)
        return simbolo if simbolo else self.global_.get_simbolo(indice)

    def imprime_fichero(self):
        with open('tabla_simbolos.txt', 'w') as f:
            for i, tabla in zip(range(1, len(self.lista_ts) + 1), self.lista_ts):
                f.write(f"TABLA {tabla.nombre} # {i} :\n")
                f.write(str(tabla))
                f.write('-------------------------------------')


class TablaSimbolo:
    def __init__(self, nombre):
        self._nombre = nombre
        self.simbolos_dict = OrderedDict()
        self.simbolos_list = []
        self.despl = 0

    @property
    def nombre(self):
        return self._nombre

    def insertar_lexema(self, lexema):
        simbolo = Simbolo(lexema)
        self.simbolos_dict[lexema] = simbolo
        self.simbolos_list.append(simbolo)
        return len(self.simbolos_list) - 1

    def posicion_lexema(self, lexema):
        if lexema in self.simbolos_dict:
            return list(self.simbolos_dict).index(lexema)
        else:
            return None

    def get_simbolo(self, indice):
        return self.simbolos_list[indice]

    def __str__(self):
        return '\n'.join([str(simbolo) for simbolo in self.simbolos_dict.values()])


class Simbolo:
    def __init__(self, lexema):
        self._lexema = lexema
        self._propiedad = {}

    @property
    def lexema(self):
        return self._lexema

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
    s = ts.get_simbolo(0)
    s.nombre = 'hello'
    print(s.nombre)
    s['tipo'] = 'funcion'
    s['numParm'] = 2
    s['tipoParam'] = 'boolean string'
    # s['tipoParam2'] = 'string'
    ts.insertar_lexema('var2')
    s = ts.get_simbolo(1)
    s['tipo'] = 'entero'
    s['despl'] = 8
    print(ts)
