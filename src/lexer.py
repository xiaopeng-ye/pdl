from sly import Lexer


class JSLexer(Lexer):
    # String containing ignored characters
    ignore = ' \t'
    ignore_comment = r'//.*'
    ignore_newline = r'\n+'
    
    #Set of token names.
    tabla_simbolos = []

    #tabla_palabra_reservada = ['alert', 'boolean', 'for', 'function', 'if', 'input', 'le', 'number', 'return', 'string', 'true', 'false']
    tabla_op_aritmetico = ['+', '-', '*', '/', '%', '++']
    tabla_op_relacional = ['==', '!=', '<', '>', '<=', '>=']
    tabla_op_logico = ['&&', '||', '!']
    
    #Regular expression rules for tokens
    Identificador = r'[a-zA-Z][a-zA-Z0-9_]*'
    Entero = r'\d+'
    Cadena = r'\'.*\''
    OpAritmetico = r'(\+\+)|(\/)|(-)|(\*)|(%)|(\+)'
    OpRelacional = r'(==)|(!=)|(<=)|(>=)|(<)|(>)'
    OpAsignacion = r'='
    OpLogico = r'(\&\&)|(\|\|)|(\!)'
    LlaveIzquierda = r'{'
    LlaveDerecha = r'}'
    ParentesisIzquierdo = r'\('
    ParentesisDerecho = r'\)'
    PuntoComa = r';'
    Coma = r','
    EOF = r''

    #Keywords
    Identificador['alert'] = ALERT
    Identificador['boolean'] = BOOLEAN
    Identificador['for'] = FOR
    Identificador['function'] = FUNCTION
    Identificador['if'] = IF
    Identificador['input'] = INPUT
    Identificador['let'] = LET
    Identificador['number'] = NUMBER
    Identificador['return'] = RETURN
    Identificador['string'] = STRING
    Identificador['true'] = TRUE
    Identificador['false'] = FALSE

    # Tokens
    tokens = {Identificador, Entero, Cadena, OpAsignacion, OpAritmetico, OpRelacional, OpLogico, LlaveIzquierda,
              LlaveDerecha, PuntoComa, Coma, EOF, ALERT, BOOLEAN, FOR, FUNCTION, IF, INPUT, LET, NUMBER, RETURN, STRING, TRUE, FALSE}

	def ignore_newline(self, token):
		self.lineno += t.value.count('\n')

    def Entero(self, token):
        token.value = int(token.value)
        return to

    @_('alert')
    def token_to_lower(self, token):
        return token.type = token.type.lower()

    def error(self, token):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1