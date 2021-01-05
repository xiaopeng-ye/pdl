from error import GestorError
from table import GestorTablaSimbolo
from lexer import JSLexer
from semantic import JSSemantic
from collections import deque
import pandas as pd
import sys


class JSParser:

    def __init__(self, path):
        self.path = path
        self.tabla = pd.read_csv('../config/descendente_tabular.csv', index_col=0, dtype=str)
        self.producciones = ['vacia']
        self.token_file = None
        self.lexico = None
        with open('../config/producciones.txt', 'r') as f:
            for line in f:
                self.producciones.append(line.strip())

        self.terminales = {'alert', 'boolean', 'for', 'function', 'if', 'input', 'let', 'number', 'return', 'string',
                           'true', 'false', 'ID', 'ENTERO', 'CADENA', '=', '+', '-', '++', '==', '!=', '&&',
                           '||', '(', ')', '{', '}', ',', ';'}
        self.no_terminales = {'P', 'B', 'S', 'C', 'E', 'Y', 'X', 'F', 'A', 'K', 'L', 'Q', 'H', 'T',
                              'R', 'I', 'U', 'O', 'V', 'J', 'W', 'D', 'G', 'M', 'N'}
        self.cast_tk = {'IDENTIFICADOR': 'ID', 'ENTERO': 'ENTERO', 'CADENA': 'CADENA', 'ASIGNACION': '=',
                        'ARITSUMA': '+', 'ARITRESTA': '-', 'ARITINCRE': '++', 'RELIGUAL': '==',
                        'RELDISTINTO': '!=', 'LOGAND': '&&',
                        'LOGOR': '||', 'LLAVEIZQ': '{', 'LLAVEDER': '}', 'PARENTESISIZQ': '(',
                        'PARENTESISDER': ')', 'PUNTOCOMA': ';', 'COMA': ',', 'ALERT': 'alert',
                        'BOOLEAN': 'boolean', 'FOR': 'for', 'FUNCTION': 'function',
                        'IF': 'if', 'INPUT': 'input', 'LET': 'let', 'NUMBER': 'number', 'RETURN': 'return',
                        'STRING': 'string', 'TRUE': 'true', 'FALSE': 'false'}

    def sig_tok(self, tks):
        try:
            token = next(tks)
        except StopIteration:
            simbolo = Simbolo('$')
            simbolo.lineno = self.lexico.lineno
            return simbolo
        self.token_file.write(f'<{token.type},{token.value}>\n')
        token.type = self.cast_tk[token.type]
        return token

    def parse(self):
        # inicializar todos los componentes
        gestor_ts = GestorTablaSimbolo()
        gestor_err = GestorError()
        self.lexico = JSLexer(gestor_ts, gestor_err)
        js_file = open(self.path, 'r')
        tks = self.lexico.tokenize(js_file.read())
        semantico = JSSemantic(self.lexico, gestor_ts, gestor_err)
        self.token_file = open('../tokens.txt', 'w')
        lista_reglas = ['Descendente']
        # algoritmo del analizador sintactico
        pila = deque([Simbolo('$'), Simbolo('P')])
        token = self.sig_tok(tks)
        x = pila[-1]
        while True:
            # print('pila:', end=' ')
            # for el in pila:
            #     print(el.type, end=',')
            # print()
            #
            # print('pila_aux:', end=' ')
            # for el in semantico.pila_aux:
            #     print(el.type, end=',')
            # print()
            # print(x.type)

            # terminal
            if x.type in self.terminales:
                # print('ejecuta terminal')
                if x.type == token.type:
                    simbolo = pila.pop()
                    simbolo.linea = token.lineno
                    if token.type == 'ID':
                        simbolo.pos = token.value
                    semantico.pila_aux.append(simbolo)
                    linea = token.lineno
                    token = self.sig_tok(tks)
                else:
                    gestor_err.imprime('Sintáctico', f'Se espera el símbolo {x.type}',
                                       token.lineno if x.type != ';' else linea)

            # no terminal
            elif x.type in self.no_terminales:
                # print('ejecuta no terminal')
                # print(token.type)
                regla = self.tabla.loc[x.type, token.type]
                if not pd.isnull(regla):
                    lista_reglas.append(regla)
                    semantico.pila_aux.append(pila.pop())
                    for elemento in reversed((self.producciones[int(regla)].split('->'))[1].strip().split(' ')):
                        if elemento != 'lambda':
                            pila.append(Simbolo(elemento))
                else:
                    gestor_err.imprime('Sintáctico',
                                       f"No se espera el símbolo '{token.type}'" if token.type != '$' else "Se espera ';'",
                                       token.lineno)

            # accion semantica
            else:
                # print('ejecuta accion semantica')
                eval('semantico.' + x.type + '()')
                pila.pop()

            x = pila[-1]

            # actualiza la tabla cada iteracion
            gestor_ts.imprime()

            if x.type == '$':
                break

        if token.type == x.type:
            print('Correcto')

        # cerrar los recursos
        with open('../parse.txt', 'w') as f:
            f.write(' '.join(lista_reglas))
        gestor_ts.imprime()
        js_file.close()
        self.token_file.close()


class Simbolo:
    # __slots__ = ('type', 'tipo', 'ret', 'ancho', 'pos', 'lexema')

    def __init__(self, valor):
        self.type = valor


if __name__ == '__main__':
    # parser = JSParser('codigo.js')
    # parser.parse()
    try:
        parser = JSParser('../codigo.js')
        parser.parse()
    except Exception as e:
        print(e, file=sys.stderr)
        print('Error encontrado', file=sys.stderr)
