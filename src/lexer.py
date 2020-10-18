from sly import Lexer


class JSLexer(Lexer):
    ignore = ' \t'
    ignore_comment = r'\\\\.*'

    tabla_simbolos = []
    tabla_palabra_reservada = ['alert', 'boolean', 'for', 'function', 'if', 'input', 'le', 'number', 'return', 'string',
                               'true', 'false']
    tabla_op_aritmetico = ['+', '-', '*', '/', '%', '++']
    tabla_op_relacional = ['==', '!=', '<', '>', '<=', '>=']
    tabla_op_logico = ['&&', '||', '!']

    Identificador = r'[a-zA-Z][a-zA-Z0-9_]*'
    Entero = r'\d+'
    Cadena = r'\'.*\''
    OpAritmetico = r'(\+\+)|(\/)|(-)|(\*)|(%)|(\+)'
    OpRelacional = r'(==)|(!=)|(<=)|(>=)|(<)|(>)'
    OpAsignacion = r'='
    OpLogico = r'(\&\&)|(\|\|)|(\!)'
    LlaveIzquierda = r'{'
    LlaveDerecha = r'}'
    PuntoComa = r';'
    Coma = r','
    EOF = r''

    tokens = {Identificador, Entero, Cadena, OpAsignacion, OpAritmetico, OpRelacional, OpLogico, LlaveIzquierda,
              LlaveDerecha, PuntoComa, Coma, EOF}