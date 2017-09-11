# -------------------------------------
# COMPILERS PROJECT: Python Interpreter
# Carlos Eduardo Vaca Guerra
# A01207563
# -------------------------------------

# List of all possible tokens allowed in my interpreter.
tokens = (    
    'COMMENT',
    'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE',
    'PLUS', 'MINUS', 'PROD', 'DIV', 'EQUALS',
    'IF', 'ELSE',
    'FOR', 'IN', 'COL',
    'INPUT', 'OUTPUT',
    'LAMBDA', 'MAP', 'REDUCE', 'FILTER',
    'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'COMA',
    'NAME', 'NUMBER',
)

# Token definition with regex.
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_PROD      = r'\*'
t_DIV       = r'/'
t_EQUALS    = r'='
t_EQ        = r'=='
t_NEQ       = r'!='
t_GT        = r'>'
t_GE        = r'>='
t_LT        = r'<'
t_LE        = r'<='
t_COMMENT   = r'\#'
t_COL       = r':'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
t_COMA      = r','
t_NAME      = r'[a-zA-Z_][a-zA-Z0-9_]*'

# TODO: ADD NOTE OF WHY USING FUNCTIONs

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_LAMBDA(t):
    r'lambda'
    return t

def t_MAP(t):
    r'map'
    return t

def t_REDUCE(t):
    r'reduce'
    return t

def t_FILTER(t):
    r'filter'
    return t

def t_INPUT(t):
    r'input'
    return t

def t_OUTPUT(t):
    r'output'
    return t


# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

while True:
    try:
        s = input('Vaca > ')
    except EOFError:
        break
    lexer.input(s)
    for token in lexer:
        print(token)
