from table import GestorTablaSimbolo
from lexer import JSLexer
from collections import deque
import pandas as pd


class JSParser:

    def __init__(self):
        self.tabla = pd.read_csv('descendente_tabular.csv', index_col=0, dtype=str)
        self.producciones = ['vacia']
        self.token_file = None
        with open('producciones.txt', 'r') as f:
            for line in f:
                self.producciones.append(line.strip())

        self.terminales = {'alert', 'boolean', 'for', 'function', 'if', 'input', 'let', 'number', 'return', 'string',
                           'true', 'false', 'ID', 'ENTERO', 'CADENA', '=', '+', '-', '++', '==', '!=', '&&',
                           '||', '(', ')', '{', '}', ',', ';'}
        self.no_terminales = {'P', 'B', 'S', 'Z', 'C', 'E', 'Y', 'X', 'F', 'A', 'K', 'L', 'Q ', 'H ', 'T ',
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
        return self.cast_tk[token.type]

    def parse(self, tks):
        self.token_file = open('tokens.txt', 'w')
        pila = deque(['$', 'P'])
        lista_reglas = ['Descendente']
        token = self.sig_tok(tks)
        x = pila[-1]
        while True:
            print(x)
            print(pila)
            if x in self.terminales:
                if x == token:
                    pila.pop()
                    token = self.sig_tok(tks)
                else:
                    print("no equipa el token:", token)
                    break
            else:
                regla = self.tabla.loc[x, token]
                print(token)
                if not pd.isnull(regla):
                    pila.pop()
                    lista_reglas.append(regla)
                    for elemento in reversed((self.producciones[int(regla)].split('->'))[1].strip().split(' ')):
                        if elemento != 'lambda':
                            pila.append(elemento)
                else:
                    print("No hay regla para seguir")
                    break
            x = pila[-1]
            if x == '$':
                break

        if token == x:
            print('accepted')
        self.token_file.close()
        return lista_reglas


if __name__ == '__main__':
    ts = GestorTablaSimbolo()
    lexer = JSLexer(ts)
    js_file = open('codigo.js', 'r')
    tokens = lexer.tokenize(js_file.read())
    parser = JSParser()
    lista = parser.parse(tokens)
    print(lista)
