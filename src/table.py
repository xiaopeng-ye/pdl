from collections import OrderedDict


class GestorTablaSimbolo:
    def __init__(self):
        self._list_ts = []
        self._global = TablaSimbolo('global')
        self._list_ts.append(self._global)
        self._actual = self._global

    def crear_tabla_simbolo(self, nombre_funcion):
        self._actual = TablaSimbolo(nombre_funcion)
        self._list_ts.append(self._actual)

    def buscar_posicion(self, lexema):
        return self._actual.buscar_posicion(lexema)

    def insertar_lexema(self, lexema):
        return self._actual.insertar_lexema(lexema)

    def imprimir(self):
        with open('tabla_simbolos.txt', 'w') as f:
            for i, tabla in zip(len(self._list_ts), self._list_ts):
                f.write(f"TABLA # {i} :")
                f.write(tabla)


class TablaSimbolo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._ts = OrderedDict()
        self._indice = -1
        self._despl = 0

    def insertar_lexema(self, lexema):
        self._ts[lexema] = None
        self._indice += 1
        return self._indice

    def buscar_posicion(self, lexema):
        if lexema in self._ts:
            return list(self._ts).index(lexema)
        else:
            return None

    def __str__(self):
        for lexema, propiedad in self._ts.items():
            print(f"* LEXEMA : '{lexema}'")
            print("ATRIBUTOS :")
            print(f"+ tipo : '{propiedad.tipo}'")
            if propiedad.despl is None:
                print(f"+ numParam : '{propiedad.num_param}'")
                for i, t_param, m_param in zip(range(1, len(propiedad.tipo_param) + 1), propiedad.tipo_param,
                                               propiedad.tipo_modo_paso):
                    print(f"+ TipoParam{i} : '{t_param}'")
                    print(f"+ ModoParam{i} : '{m_param}'")
            else:
                print(f"+ despl : {propiedad.despl}")


class Propiedad:
    def __init__(self, tipo, despl=None, num_param=None, tipo_param=None, modo_paso=None, tipo_dev=None, etiq=None):
        self._tipo = tipo
        self._despl = despl
        self._num_param = num_param
        self._tipo_param = tipo_param
        self._modo_paso = modo_paso
        self._tipo_dev = tipo_dev
        self._etiq = etiq

    @property
    def tipo(self):
        return self._tipo

    @property
    def despl(self):
        return self._despl

    @property
    def num_param(self):
        return self._num_param

    @property
    def tipo_param(self):
        return self._tipo_param

    @property
    def modo_paso(self):
        return self._modo_paso

    @property
    def tipo_dev(self):
        return self._tipo_dev

    @property
    def etiq(self):
        return self._etiq

# ts = TablaSimbolo("Global")
# ts.insertar_lexema('id1')
# ts.insertar_propiedad('id1', 'logica')
# ts.insertar_lexema('id2')
# ts.insertar_propiedad('id2', 'entero')
# ts.insertar_lexema('funcion1')
# ts.insertar_lexema('funcion1')
# ts.insertar_lexema('id3')
# ts.insertar_propiedad('id3', 'cadena')
# print(ts)
