# -------------------------------------
# COMPILERS PROJECT: Python Interpreter
# Carlos Eduardo Vaca Guerra
# A01207563
# -------------------------------------
import ply.lex as lex
import ply.yacc as yacc
import functools

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
            current_symbol = symbol
        else:
            #TODO: Missing lists!
            current_symbol = symbol
        self.table[id_name+'-'+str(scope)] = (symbol_type, current_symbol, scope)

    def get_element(self, symbol, scope):
        return self.table.get(symbol+'-'+str(scope), None)


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
    'LPAREN', 'RPAREN', 'LSQUARE', 'RSQUARE',
    'ID', 'NUMBER', 'COL', 'SEMI', 'COMA',
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
def p_declarationList(p):
    '''declarationList  : declaration declarationList
                        | declaration'''
    pass

# 2
def p_declaration(p):
    '''declaration  : varDeclaration SEMI
                    | statement'''
    pass

# 3
def p_varDeclaration(p):
    'varDeclaration   : ID EQUALS declarationElement'
    symbol_table.add_symbol(p[1], '', p[3], current_scope)

# 4
def p_declarationElement(p):
    '''declarationElement   : list
                            | expressionStmt
                            | STRING                        
                            | BOOLEAN
                            | inputStmt
                            | functionalStmt'''
    p[0] = p[1]

# 5
def p_list(p):
    'list   : LSQUARE listElements RSQUARE'
    p[0] = p[2]

# 6
def p_listElements(p):
    '''listElements : NUMBER
                    | NUMBER OP_NUMBER
                    | STRING
                    | STRING OP_STRING
                    | BOOLEAN
                    | BOOLEAN OP_BOOLEAN'''
    if len(p) == 2:
        if p[1] == 'true' or p[1] == 'false':
            p[0] = [True if p[1] == 'true' else False]
        else:
            p[0] = [p[1]]
    else:
        elements = p[2].split(',')[1:]
        if p[1] == 'true' or p[1] == 'false':
            p[0] = [True if p[1] == 'true' else False] + [True if x == 'true' else False for x in elements]
        elif isinstance(p[1], int):
            p[0] = [p[1]] + [int(x) for x in elements]
        else:
            p[0] = [p[1]] + [x for x in elements]

# 7
def p_statement(p):
    '''statement    : expressionStmt SEMI
                    | conditionalStmt
                    | iterationStmt
                    | functionalStmt SEMI
                    | inputStmt SEMI
                    | outputStmt SEMI
                    | commentStmt'''
    p[0] = p[1]

# 8
def p_iterationStmt(p):
    'iterationStmt    : FOR ID IN iterationElement COL declarationList'
    pass

# 9
def p_iterationElement(p):
    '''iterationElement : list
                        | ID'''
    p[0] = p[1]

# 10
def p_conditionalStmt(p):
    '''conditionalStmt  : IF expressionStmt COL declarationList
                        | IF expressionStmt COL declarationList ELSE COL declarationList'''
    pass

# 11
def p_expressionStmt(p):
    '''expressionStmt   : expressionStmt OR andExpression
                        | andExpression'''
    p[0] = p[1] or p[3] if len(p) > 2 else p[1]

# 12
def p_andExpression(p):
    '''andExpression    : andExpression AND unaryRelExpression
                        | unaryRelExpression'''
    p[0] = p[1] and p[3] if len(p) > 2 else p[1]

# 13
def p_unaryRelExpression(p):
    '''unaryRelExpression   : NOT unaryRelExpression
                            | relExpression'''
    p[0] = not p[2] if len(p) > 2 else p[1]

# 14
def p_relExpression(p):
    '''relExpression    : sumExpression relop sumExpression
                        | sumExpression'''
    if len(p) > 2:
        if (isinstance(p[1], list) and not isinstance(p[3], list)) or (not isinstance(p[1], list) and isinstance(p[3], list)):
            temp_list = p[1] if isinstance(p[1], list) else p[3]
            temp_value = p[1] if not isinstance(p[1], list) else p[3]
            if p[2] == '<': p[0] = [x for x in temp_list if x < temp_value]
            if p[2] == '<=': p[0] = [x for x in temp_list if x <= temp_value]
            if p[2] == '>': p[0] = [x for x in temp_list if x > temp_value]
            if p[2] == '<=': p[0] = [x for x in temp_list if x <= temp_value]
            if p[2] == '==': p[0] = [x for x in temp_list if x == temp_value]
            if p[2] == '!=': p[0] = [x for x in temp_list if x != temp_value]
        else:
            if p[2] == '<': p[0] = p[1] < p[3]
            if p[2] == '<=': p[0] = p[1] <= p[3]
            if p[2] == '>': p[0] = p[1] > p[3]
            if p[2] == '>=': p[0] = p[1] >= p[3]
            if p[2] == '==': p[0] = p[1] == p[3]
            if p[2] == '!=': p[0] = p[1] != p[3]
    else:
        p[0] = p[1]

# 15
def p_relop(p):
    '''relop    : LE
                | LT
                | GT
                | GE
                | EQ
                | NEQ'''
    p[0] = p[1]

# 16
def p_sumExpression(p):
    '''sumExpression    : sumExpression sumop term
                        | term'''
    if len(p) > 2:
        if (isinstance(p[1], list) and not isinstance(p[3], list)) or (not isinstance(p[1], list) and isinstance(p[3], list)):
            temp_list = p[1] if isinstance(p[1], list) else p[3]
            temp_value = p[1] if not isinstance(p[1], list) else p[3]
            p[0] = [x+temp_value if p[2] == '+' else x-temp_value for x in temp_list]
        else:
            if p[2] == '+': p[0] = p[1] + p[3]
            if p[2] == '-': p[0] = p[1] - p[3]
    else:
        p[0] = p[1]

# 17
def p_sumop(p):
    '''sumop    : PLUS
                | MINUS'''
    p[0] = p[1]

# 18
def p_term(p):
    '''term : term mulop sumElement
            | sumElement'''
    if len(p) > 2:
        if (isinstance(p[1], list) and not isinstance(p[3], list)) or (not isinstance(p[1], list) and isinstance(p[3], list)):
            temp_list = p[1] if isinstance(p[1], list) else p[3]
            temp_value = p[1] if not isinstance(p[1], list) else p[3]
            p[0] = [x*temp_value if p[2] == '*' else x/temp_value for x in temp_list]
        else:
            if p[2] == '*': p[0] = p[1] * p[3]
            if p[2] == '/': p[0] = p[1] / p[3]
    else:
        p[0] = p[1]

# 19
def p_sumElement(p):
    '''sumElement   : ID
                    | NUMBER'''    
    if not str(p[1])[0].isdigit():
        value = symbol_table.get_element(p[1], current_scope)
        if value:
            p[0] = value[1]
        else:
            print("Undefined name {}".format(p[1]))
            p[0] = 0        
    else:        
        p[0] = p[1]

# 20
def p_mulop(p):
    '''mulop    : PROD
                | DIV'''
    p[0] = p[1]

# 21
def p_functionalStmt(p):
    '''functionalStmt   : FILTER LPAREN lambdaFilter RPAREN
                        | MAP LPAREN lambdaMap RPAREN
                        | REDUCE LPAREN lambdaReduce RPAREN'''
    p[0] = p[3]

# 22
def p_lambdaMap(p):
    'lambdaMap   : LAMBDA COL sumExpression'    
    p[0] = p[3]

# 23
def p_lambdaReduce(p):
    '''lambdaReduce : LAMBDA COL mulop COMA ID
                    | LAMBDA COL sumop COMA ID'''
    current_id = symbol_table.get_element(p[5], current_scope)
    if current_id:
        if p[3] == '+': p[0] = functools.reduce(lambda x,y: x+y, current_id[1])
        if p[3] == '-': p[0] = functools.reduce(lambda x,y: x-y, current_id[1])
        if p[3] == '/': p[0] = functools.reduce(lambda x,y: x/y, current_id[1])
        if p[3] == '*': p[0] = functools.reduce(lambda x,y: x*y, current_id[1])
    else:
        print("Undefined name {}".format(p[5]))
        p[0] = 0

# 24
def p_lambdaFilter(p):
    'lambdaFilter : LAMBDA COL relExpression'
    p[0] = p[3]

# 25
def p_inputStmt(p):
    'inputStmt  : INPUT LPAREN RPAREN'
    p[0] = input()

# 26
def p_outputStmt(p):
    'outputStmt : OUTPUT LPAREN declarationElement RPAREN'
    print(p[3])

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
