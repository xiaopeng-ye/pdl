from table import GestorTablaSimbolo
from lexer import JSLexer
from semantic import JSSemantic
from collections import deque
import pandas as pd


class JSParser:

    def __init__(self, path):
        self.path = path
        self.tabla = pd.read_csv('descendente_tabular.csv', index_col=0, dtype=str)
        self.producciones = ['vacia']
        self.token_file = None
        with open('producciones.txt', 'r') as f:
            for line in f:
                self.producciones.append(line.strip())

        self.terminales = {'alert', 'boolean', 'for', 'function', 'if', 'input', 'let', 'number', 'return', 'string',
                           'true', 'false', 'ID', 'ENTERO', 'CADENA', '=', '+', '-', '++', '==', '!=', '&&',
                           '||', '(', ')', '{', '}', ',', ';'}
        self.no_terminales = {'P', 'B', 'S', 'C', 'E', 'Y', 'X', 'F', 'A', 'K', 'L', 'Q ', 'H ', 'T ',
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
            return '$'
        self.token_file.write(f'<{token.type},{token.value}>\n')
        token.type = self.cast_tk[token.type]
        return token

    def parse(self):
        # inicializar todos los componentes
        ts = GestorTablaSimbolo()
        lexico = JSLexer(ts)
        js_file = open(self.path, 'r')
        tks = lexico.tokenize(js_file.read())
        semantico = JSSemantic(ts)
        self.token_file = open('tokens.txt', 'w')
        lista_reglas = ['Descendente']
        # algoritmo del analizador sintactico
        pila = deque([Simbolo('$'), Simbolo('P')])
        token = self.sig_tok(tks)
        x = pila[-1]
        while True:
            print(x.valor)
            print('pila:', end=' ')
            for e in pila:
                print(e.valor, end=',')
            print()

            # terminal
            if x.valor in self.terminales:
                if x.valor == token.type:
                    simbolo = pila.pop()
                    if token.type == 'ID':
                        simbolo.pos = token.value
                    semantico.pila_aux.append(simbolo)
                    token = self.sig_tok(tks)
                else:
                    print("no equipa el token:", token.type)
                    break

            # no terminal
            elif x.valor in self.no_terminales:
                # print(x)
                # print(token)
                regla = self.tabla.loc[x.valor, token.type]
                if not pd.isnull(regla):
                    lista_reglas.append(regla)
                    semantico.pila_aux.append(pila.pop())
                    for elemento in reversed((self.producciones[int(regla)].split('->'))[1].strip().split(' ')):
                        if elemento != 'lambda':
                            pila.append(Simbolo(elemento))
                else:
                    print("No hay regla para seguir")
                    break

            # accion semantica
            else:
                eval('semantico.' + simbolo.valor + '()')
                pila.pop()

            x = pila[-1]
            if x == '$':
                break

        if token == x:
            print('Accepted')

        # cerrar los recursos
        with open('parse.txt', 'w') as f:
            f.write(' '.join(lista_reglas))
        ts.imprime_fichero()
        js_file.close()
        self.token_file.close()


class Simbolo:

    def __init__(self, valor):
        self.valor = valor


if __name__ == '__main__':
    parser = JSParser('codigo.js')
    parser.parse()
