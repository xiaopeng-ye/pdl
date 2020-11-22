from sly import Lexer
from table import GestorTablaSimbolo
import re


class JSLexer(Lexer):

    def __init__(self, gestor_ts):
        self._gestor_ts = gestor_ts

    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'//.*'
    ignore_newline = r'\n+'

    # Keywords and identifiers
    IDENTIFICADOR = r'[a-zA-Z][a-zA-Z0-9_]*'
    IDENTIFICADOR['alert'] = ALERT
    IDENTIFICADOR['boolean'] = BOOLEAN
    IDENTIFICADOR['for'] = FOR
    IDENTIFICADOR['function'] = FUNCTION
    IDENTIFICADOR['if'] = IF
    IDENTIFICADOR['input'] = INPUT
    IDENTIFICADOR['let'] = LET
    IDENTIFICADOR['number'] = NUMBER
    IDENTIFICADOR['return'] = RETURN
    IDENTIFICADOR['string'] = STRING
    IDENTIFICADOR['true'] = TRUE
    IDENTIFICADOR['false'] = FALSE

    # Tokens
    tokens = {IDENTIFICADOR, ENTERO, CADENA, ASIGNACION, ARITSUMA, ARITRESTA, ARITINCRE, RELIGUAL, RELDISTINTO, LOGAND,
              LOGOR, LLAVEIZQ, LLAVEDER, PARENTESISIZQ, PARENTESISDER, PUNTOCOMA, COMA, ALERT, BOOLEAN, FOR, FUNCTION,
              IF, INPUT, LET, NUMBER, RETURN, STRING, TRUE, FALSE}

    # Methods for tokens
    @_(r'\d+')
    def ENTERO(self, token):
        token.value = int(token.value)
        if -32767 < token.value < 32767:
            return token
        else:
            print('Línea %d: Valor incorrecto, debe corresponder a un número de 16 bits' % self.lineno)

    @_(r'\'.*\'')
    def CADENA(self, token):
        token.value = re.sub(r"\\\'", "'", token.value)
        token.value = re.sub(r'\\\\', r'\\', token.value)
        token.value = u'"{cadena}"'.format(cadena=token.value.strip("'"))
        return token

    @_(r'\+\+')
    def ARITINCRE(self, token):
        token.value = ''
        return token

    @_(r'-')
    def ARITRESTA(self, token):
        token.value = ''
        return token

    @_(r'\+')
    def ARITSUMA(self, token):
        token.value = ''
        return token

    @_(r'==')
    def RELIGUAL(self, token):
        token.value = ''
        return token

    @_(r'!=')
    def RELDISTINTO(self, token):
        token.value = ''
        return token

    @_(r'(\&\&)')
    def LOGAND(self, token):
        token.value = ''
        return token

    @_(r'(\|\|)')
    def LOGOR(self, token):
        token.value = ''
        return token

    @_(r'=')
    def ASIGNACION(self, token):
        token.value = ''
        return token

    @_(r'{')
    def LLAVEIZQ(self, token):
        token.value = ''
        return token

    @_(r'}')
    def LLAVEDER(self, token):
        token.value = ''
        return token

    @_(r'\(')
    def PARENTESISIZQ(self, token):
        token.value = ''
        return token

    @_(r'\)')
    def PARENTESISDER(self, token):
        token.value = ''
        return token

    @_(r';')
    def PUNTOCOMA(self, token):
        token.value = ''
        return token

    @_(r',')
    def COMA(self, token):
        token.value = ''
        return token

    def IDENTIFICADOR(self, token):
        if len(token.value) > 64:
            print('Línea %d: Tamaño de cadena inválido, debe ser menor de 64 caracteres' % self.lineno)
        else:
            indice = self._gestor_ts.busca_ts(token.value)
            if indice is None:
                token.value = self._gestor_ts.inserta_ts(token.value)
            else:
                token.value = indice
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def ALERT(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def BOOLEAN(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def FOR(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def FUNCTION(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def IF(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def INPUT(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def LET(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def NUMBER(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def RETURN(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def STRING(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def TRUE(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    @_(r'[a-zA-Z][a-zA-Z0-9_]*')
    def FALSE(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    # Line number tracking
    def ignore_newline(self, token):
        self.lineno += token.value.count('\n')

    def error(self, token):
        print('Línea %d: Caracter erróneo %r' % (self.lineno, token.value[0]))
        self.index += 1


js_file = open('codigo.js', 'r')
token_file = open('tokens.txt', 'w')
ts = GestorTablaSimbolo()
lexer = JSLexer(ts)

for token in lexer.tokenize(js_file.read()):
    token_file.write(f'<{token.type},{token.value}>\n')

ts.imprime_fichero()
token_file.close()
js_file.close()
