# -------------------------------------
# COMPILERS PROJECT: Python Interpreter
# Carlos Eduardo Vaca Guerra
# A01207563
# -------------------------------------
import ply.lex as lex
import ply.yacc as yacc

class SymbolTable(object):
    """Structure for storing symbols.
    { 'ID-Scope': (Type, Value, Scope)}
    """

    def __init__(self):
        self.table = {}
    
    def __str__(self):
        return str(self.table)

    def add_symbol(self, id_name, symbol_type, symbol, scope):
        """Adds a symbol to the table
        PARAMS:
        - id_name : Name of ID
        - symbol_type : Type of the symbol
        - symbol : Symbol to be stored
        - scope : Current scope
        """
        current_symbol = 0
        if symbol_type == 'STRING':
            current_symbol = symbol[1:-1]
        elif symbol_type == 'BOOLEAN':
            current_symbol = True if symbol == 'true' else False
        elif symbol_type == 'NUMBER':
            current_symbol = int(symbol)
        else:
            #TODO: Missing lists!
            current_symbol = symbol
        self.table[id_name+'-'+str(scope)] = (symbol_type, current_symbol, scope)

# Dictionary for reserverd words. { reserved_word : token }
reserved_words = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'in': 'IN',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'lambda': 'LAMBDA',
    'map': 'MAP',
    'reduce': 'REDUCE',
    'filter': 'FILTER',
    'input': 'INPUT',
    'print': 'OUTPUT',
}

# List of all possible tokens allowed in my interpreter.
tokens = [    
    'COMMENT', 'STRING', 'OP_STRING', 'OP_NUMBER', 'BOOLEAN', 'OP_BOOLEAN',
    'EQ', 'NEQ', 'GT', 'GE', 'LT', 'LE',
    'PLUS', 'MINUS', 'PROD', 'DIV', 'EQUALS',
    'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE', 'COMA',
    'ID', 'OP_ID', 'NUMBER', 'COL', 'SEMI',
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
t_COL       = r':'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LSQUARE   = r'\['
t_RSQUARE   = r'\]'
t_COMA      = r','
t_SEMI      = r';'

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

def t_OP_NUMBER(t):
    r'(,\d+)+'    
    return t

def t_COMMENT(t):
    r'\#.*'
    return t

def t_OP_STRING(t):
    r'(,\'[^\']*\')+'    
    return t

def t_STRING(t):
    r'\'[^\']*\''    
    return t

def t_OP_BOOLEAN(t):
    r'(,(true|false))+' 
    return t

def t_BOOLEAN(t):
    r'true|false'
    return t

def t_OP_ID(t):
    r'(,[a-zA-Z_][a-zA-Z0-9_]*)+'
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
    print("ERROR: Illegal symbol '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Scope tracker
current_scope = 0

# Symbol table for IDs
symbol_table = SymbolTable()

# Parser rules

# 1
def p_declarationList(t):
    '''declarationList  : declaration declarationList
                        | declaration'''
    pass

# 2
def p_declaration(t):
    '''declaration  : varDeclaration SEMI
                    | statement'''
    pass

# 3
def p_varDeclaration(p):
    'varDeclaration   : ID EQUALS declarationElement'
    lexer.input(p[3])
    symbol_table.add_symbol(p[1], lexer.token().type, p[3], current_scope)

# 4
def p_declarationElement(p):
    '''declarationElement   : list
                            | sumExpression
                            | STRING                        
                            | BOOLEAN'''
    p[0] = p[1]

# 5
def p_list(t):
    'list   : LSQUARE listElements RSQUARE'
    pass

# 6
def p_listElements(t):
    '''listElements : NUMBER
                    | NUMBER OP_NUMBER
                    | STRING
                    | STRING OP_STRING
                    | BOOLEAN
                    | BOOLEAN OP_BOOLEAN'''
    pass

# 7
def p_statement(t):
    '''statement    : expressionStmt SEMI
                    | conditionalStmt
                    | iterationStmt
                    | functionalStmt SEMI
                    | inputStmt SEMI
                    | outputStmt SEMI
                    | commentStmt'''
    pass

# 8
def p_iterationStmt(t):
    'iterationStmt    : FOR ID IN iterationElement COL declarationList'
    pass

# 9
def p_iterationElement(t):
    '''iterationElement : list
                        | ID'''
    pass

# 10
def p_conditionalStmt(t):
    '''conditionalStmt  : IF expressionStmt COL declarationList
                        | IF expressionStmt COL declarationList ELSE COL declarationList'''
    pass

# 11
def p_expressionStmt(t):
    '''expressionStmt   : expressionStmt OR andExpression
                        | andExpression'''
    pass

# 12
def p_andExpression(t):
    '''andExpression    : andExpression AND unaryRelExpression
                        | unaryRelExpression'''
    pass

# 13
def p_unaryRelExpression(t):
    '''unaryRelExpression   : NOT unaryRelExpression
                            | relExpression'''
    pass

# 14
def p_relExpression(t):
    '''relExpression    : sumExpression relop sumExpression
                        | sumExpression'''
    pass

# 15
def p_relop(t):
    '''relop    : LE
                | LT
                | GT
                | GE
                | EQ
                | NEQ'''
    pass

# 16
def p_sumExpression(t):
    '''sumExpression    : sumExpression sumop term
                        | term'''
    pass

# 17
def p_sumop(t):
    '''sumop    : PLUS
                | MINUS'''
    pass

# 18
def p_term(t):
    '''term : term mulop sumElement
            | sumElement'''
    pass

# 19
def p_sumElement(p):
    '''sumElement   : ID
                    | NUMBER'''
    lexer.input(str(p[1]))
    if lexer.token().type == 'ID':
        try:
            symbol = symbol_table[p[1]+'-'+str(current_scope)]
            p[0] = symbol[1]
        except LookupError:
            print("Undefined name {}".format(p[1]))
            p[0] = 0
    else:
        print('RETURNING {}'.format(p[1]))
        p[0] = p[1]

# 20
def p_mulop(t):
    '''mulop    : PROD
                | DIV'''
    pass

# 21
def p_functionalStmt(t):
    '''functionalStmt   : FILTER LPAREN lambdaFilter RPAREN
                        | MAP LPAREN lambdaStmt RPAREN
                        | REDUCE LPAREN lambdaStmt RPAREN'''
    pass

# 22
def p_lambdaStmt(t):
    '''lambdaStmt   : LAMBDA lambdaElement COL sumExpression COMA iterationElement'''
    pass

def p_lambdaElement(t):
    '''lambdaElement    : ID
                        | ID OP_ID'''
    pass

# 23
def p_lambdaFilter(t):
    'lambdaFilter : LAMBDA lambdaElement COL expressionStmt COMA iterationElement'
    pass

# 24
def p_inputStmt(t):
    'inputStmt  : INPUT LPAREN RPAREN'
    pass

# 25
def p_outputStmt(t):
    'outputStmt : OUTPUT LPAREN declarationElement RPAREN'
    pass

def p_commentStmt(t):
    'commentStmt    : COMMENT'
    pass

def p_error(t):
    if t:
        print("Syntax error at '%s'" % t.value)
    else:
        print('Syntax error at EOF')

parser = yacc.yacc()

def main():
    """Main function to be run at execution.
    """
    while True:
        try:
            s = input('Cowpy > ')
        except EOFError:
            break
        parser.parse(s)
        print(symbol_table)

if __name__ == '__main__':
    main()
