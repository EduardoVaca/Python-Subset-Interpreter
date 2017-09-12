# -------------------------------------
# COMPILERS PROJECT: Python Interpreter
# Carlos Eduardo Vaca Guerra
# A01207563
# -------------------------------------
import ply.lex as lex

# Dictionary for reserverd words. { reserved_word : token }
reserved_words = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'lambda': 'LAMBDA',
    'map': 'MAP',
    'reduce': 'REDUCE',
    'filter': 'FILTER',
    'input': 'INPUT',
    'output': 'OUTPUT',
}

# List of all possible tokens allowed in my interpreter.
tokens = [    
    'COMMENT', 'STRING',
    'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE',
    'PLUS', 'MINUS', 'PROD', 'DIV', 'EQUALS',
    'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'COMA',
    'ID', 'NUMBER', 'COL',
] + list(reserved_words.values())

# Token definition with regex.
# Each token has a matching declarationof form: t_TOKNAME
# (must match with token name from tokens list)
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

# More complex tokens are defined with functions.
# Hierarchy is set by order of func definition.
def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\'.*\''
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved_words.get(t.value, 'ID')    # Check for reserved words
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
   
def t_error(t):
    """Method that defines behavior in case an error is found at tokenizing.
    """
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def main():
    """Main function to be run at execution.
    """
    while True:
        try:
            s = input('Vaca > ')
        except EOFError:
            break
        lexer.input(s)
        for token in lexer:
            print(token)

if __name__ == '__main__':
    main()
