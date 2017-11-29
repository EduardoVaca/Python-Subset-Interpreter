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
        """Gets and element from symbol table
        PARAMS:
        - symbol : name of symbol to be fetched
        - scope : scope of symbol
        RETURNS:
        - value if symbol found, None if not
        """
        return self.table.get(symbol+'-'+str(scope), None)

symbol_table = SymbolTable()

class Node(object):

    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Number(Node):
    
    def __init__(self, value):
        self.type = 'NUMBER'
        self.value = value

    def execute(self):
        return self.value

class ID(Node):

    def __init__(self, name, scope):
        self.name = name
        self.type = 'ID'
        self.scope = scope
    
    def execute(self):
        value = symbol_table.get_element(self.name, self.scope)
        if value:
            return value[1]
        else:
            print("Undefined name {}".format(p[1]))
            return 0 # Maybe None

class BinaryOp(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'BINARY_OP'

    def execute(self):
        if self.op == '+': return self.left.execute() + self.right.execute()
        if self.op == '-': return self.left.execute() - self.right.execute()
        if self.op == '*': return self.left.execute() * self.right.execute()
        if self.op == '/': return self.left.execute() / self.right.execute()
        else: return 0

symbol_table.add_symbol('x', '', 10, 0)
n = Number(12)
print(n.execute())
i = ID('x', 0)
print(i.execute())
bop = BinaryOp(i, '+', n)
print(bop.execute())