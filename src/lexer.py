from sly import Lexer
from sly.lex import Token

# tabla_palabra_reservada = ['alert', 'boolean', 'for', 'function', 'if', 'input', 'le', 'number', 'return', 'string', 'true', 'false']


class JSLexer(Lexer):

    def __init__(self):
        self.tabla_op_aritmetico = ['+', '-', '*', '/', '%', '++']
        self.tabla_op_relacional = ['==', '!=', '<', '>', '<=', '>=']
        self.tabla_op_logico = ['&&', '||', '!']

    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'//.*'
    ignore_newline = r'\n+'

    #ALERT, BOOLEAN, FOR, FUNCTION, IF, INPUT, LET, NUMBER, RETURN, STRING, TRUE, FALSE

    # Regular expression rules for tokens, se va a borrar todo
    # ARITMETICO = r'(\+\+)|(\/)|(-)|(\*)|(%)|(\+)'
    # RELACIONAL = r'(==)|(!=)|(<=)|(>=)|(<)|(>)'
    # ASIGNACION, = r'='
    # LOGICO = r'(\&\&)|(\|\|)|(\!)'
    # LLAVEIZQ = r'{'
    # LLAVEDER = r'}'
    # PARENTESISIZQ = r'\('
    # PARENTESISDER = r'\)'
    # PUNTO_COMA = r';'
    # COMA = r','

    # # Keywords
    # IDENTIFICADOR['alert'] = ALERT
    # IDENTIFICADOR['boolean'] = BOOLEAN
    # IDENTIFICADOR['for'] = FOR
    # IDENTIFICADOR['function'] = FUNCTION
    # IDENTIFICADOR['if'] = IF
    # IDENTIFICADOR['input'] = INPUT
    # IDENTIFICADOR['let'] = LET
    # IDENTIFICADOR['number'] = NUMBER
    # IDENTIFICADOR['return'] = RETURN
    # IDENTIFICADOR['string'] = STRING
    # IDENTIFICADOR['true'] = TRUE
    # IDENTIFICADOR['false'] = FALSE

    # Tokens
    tokens = {IDENTIFICADOR, ENTERO, CADENA, ASIGNACION, ARITMETICO, RELACIONAL, LOGICO, LLAVEIZQ,
              LLAVEDER, PARENTESISIZQ, PARENTESISDER, PUNTOCOMA, COMA, PALABRA_RESERVADA}

    # Methods for tokens
    @_(r'\d+')
    def ENTERO(self, token):
        token.value = int(token.value)
        return token

    @_(r'\'.*\'')
    def CADENA(self, token):
        token.value = u'"{cadena}"'.format(cadena=token.value.strip("'"))
        return token

    @_(r'\+\+', r'\/', r'-', r'\*', r'%', r'\+')
    def ARITMETICO(self, token):
        token.value = self.tabla_op_aritmetico.index(token.value)
        return token

    @_(r'==', r'!=', r'<=', r'>=', r'<', r'>')
    def RELACIONAL(self, token):
        token.value = self.tabla_op_relacional.index(token.value)
        return token

    @_(r'(\&\&)', r'(\|\|)', r'(\!)')
    def LOGICO(self, token):
        token.value = self.tabla_op_logico.index(token.value)
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

    @_('alert', 'boolean', 'for', 'function', 'if', 'input', 'let', 'number', 'return', 'string', 'true', 'false')
    def PALABRA_RESERVADA(self, token):
        token.type = token.value.upper()
        token.value = ''
        return token

    IDENTIFICADOR = r'[a-zA-Z][a-zA-Z0-9_]*'

    # Line number tracking
    def ignore_newline(self, token):
        self.lineno += token.value.count('\n')

    def error(self, token):
        print('Line %d: Bad character %r' % (self.lineno, token.value[0]))
        self.index += 1


data = '''    
let string s;	// variable global cadena

function number FactorialRecursivo (number n)	//
{
    if (n == 0)	return 1;
	return n * FactorialRecursivo (n - 1);	//
}

let number uno = 1;	// la inicialización es de implementación opcional
let number UNO = uno;

function string salto ()
{
    return 'fgds';
}
'''
js_file = open('codigo.txt', 'r')
token_file = open('tokens.txt', 'w')
lexer = JSLexer()

for token in lexer.tokenize(js_file.read()):
    token_file.write(f'<{token.type}, {token.value}>\n')
    #token_file.write('<' + '{},{}'.format(token.type, token.value) + '>\n')

token_file.close()
