from table import GestorTablaSimbolo
from lexer import JSLexer


class JSParser:

    def __init__(self, lexico):
        self.list_reglas = []
        self.lexico = lexico


if __name__ == '__main__':
    ts = GestorTablaSimbolo()
    lexer = JSLexer(ts)
    js_file = open('codigo.js', 'r')
    tokens = lexer.tokenize(js_file.read())
    print(next(tokens).type)
    print(next(tokens).type)
    print(next(tokens).type)
    print(next(tokens).type)
    print(next(tokens).type)
