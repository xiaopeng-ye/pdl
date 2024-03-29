from collections import OrderedDict


class GestorTablaSimbolo:
    def __init__(self):
        self.lista_ts = []
        self.global_ = TablaSimbolo('global')
        self.lista_ts.append(self.global_)
        self.actual = self.global_
        self.zona_decl = False
        self.indice = -1

    def crea_tabla(self, indice):
        self.actual = TablaSimbolo(self.global_.get_simbolo(indice).lexema)
        self.lista_ts.append(self.actual)

    def libera_tabla(self):
        self.actual = self.global_

    def busca_ts(self, lexema):
        index = self.actual.posicion_lexema(lexema)
        return self.global_.posicion_lexema(lexema) if index is None else index

    def busca_ts_activa(self, lexema):
        return self.actual.posicion_lexema(lexema)

    def inserta_ts_activa(self, lexema):
        self.indice += 1
        self.actual.insertar_lexema(self.indice, lexema)
        return self.indice

    def inserta_ts_global(self, lexema):
        self.indice += 1
        self.global_.insertar_lexema(self.indice, lexema)
        return self.indice

    def aniadir_var_atributos_ts_activa(self, indice, tipo, tam):
        simbolo = self.actual.get_simbolo(indice)
        simbolo['tipo'] = tipo
        simbolo['despl'] = self.actual.despl
        self.actual.despl += tam

    def aniadir_var_atributos_ts_global(self, indice, tipo, tam):
        simbolo = self.global_.get_simbolo(indice)
        simbolo['tipo'] = tipo
        simbolo['despl'] = self.actual.despl
        self.actual.despl += tam

    def aniadir_func_atributos_ts(self, indice, tipo_param, tipo_retorno):
        simbolo = self.global_.get_simbolo(indice)
        simbolo['tipo'] = 'funcion'
        simbolo['etiqFuncion'] = simbolo.lexema
        simbolo['tipoRetorno'] = tipo_retorno

        if tipo_param != 'vacio':
            simbolo['tipoParam'] = tipo_param
            simbolo['numParam'] = len(tipo_param.split(' '))
        else:
            simbolo['numParam'] = 0

    def buscar_simbolo_ts(self, indice):
        simbolo = self.actual.get_simbolo(indice)
        return self.global_.get_simbolo(indice) if simbolo is None else simbolo

    def imprime(self):
        with open('tabla_simbolos.txt', 'w') as f:
            for i, tabla in zip(range(1, len(self.lista_ts) + 1), self.lista_ts):
                f.write(f"TABLA {tabla.nombre} # {i} :\n")
                f.write(str(tabla))
                f.write('\n-------------------------------------\n\n')


class TablaSimbolo:
    def __init__(self, nombre):
        self._nombre = nombre
        self.simbolos_dict = OrderedDict()
        self.simbolos_list = {}
        self.despl = 0

    @property
    def nombre(self):
        return self._nombre

    def insertar_lexema(self, indice, lexema):
        simbolo = Simbolo(indice, lexema)
        self.simbolos_dict[lexema] = simbolo
        self.simbolos_list[indice] = simbolo

    def posicion_lexema(self, lexema):
        return self.simbolos_dict[lexema].indice if lexema in self.simbolos_dict else None

    def get_simbolo(self, indice):
        try:
            return self.simbolos_list[indice]
        except KeyError:
            return None

    def __str__(self):
        return '\n'.join([str(simbolo) for simbolo in self.simbolos_dict.values()])


class Simbolo:
    def __init__(self, indice, lexema):
        self._indice = indice
        self._lexema = lexema
        self._propiedad = {}

    @property
    def indice(self):
        return self._indice

    @property
    def lexema(self):
        return self._lexema

    def __setitem__(self, key, value):
        self._propiedad[key] = value

    def __getitem__(self, key):
        return self._propiedad[key] if key in self._propiedad else 'vacio'

    def __str__(self):
        cadena = f"* LEXEMA : '{self._lexema}'\n  ATRIBUTOS :\n" + ''.join(
            [u"  + {key} : {value}\n".format(key=key, value=("'" + value + "'") if isinstance(value, str) else value)
             for key, value in self._propiedad.items() if key != 'tipoParam'])
        if 'tipoParam' in self._propiedad:
            cadena += ''.join([u"  + tipoParam{i} : {value}\n".format(i=i, value=("'" + value + "'")) for value, i in
                               zip(self._propiedad['tipoParam'].split(' '), range(1, self._propiedad['numParam'] + 1))])
        return cadena


if __name__ == '__main__':
    ts = TablaSimbolo('Global')
    ts.insertar_lexema('factorial')
    s = ts.get_simbolo_lex(0)
    s.nombre = 'hello'
    print(s.nombre)
    s['tipo'] = 'funcion'
    s['numParm'] = 2
    s['tipoParam'] = 'boolean string'
    # s['tipoParam2'] = 'string'
    ts.insertar_lexema('var2')
    s = ts.get_simbolo_lex(1)
    s['tipo'] = 'entero'
    s['despl'] = 8
    print(ts)
