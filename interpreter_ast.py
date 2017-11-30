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
        """Gets and element from symbol table
        PARAMS:
        - symbol : name of symbol to be fetched
        - scope : scope of symbol
        RETURNS:
        - value if symbol found, None if not
        """
        return self.table.get(symbol+'-'+str(scope), None)

    def remove_element(self, symbol, scope):
        del self.table[symbol+'-'+str(scope)]

symbol_table = SymbolTable()

class Node(object):

    def execute(self):
        raise NotImplementedError("Subclass must implement abstract method")

class DeclarationList(Node):

    def __init__(self, declaration, declaration_list=None):
        self.type = 'DECLARATION_LIST'
        self.declaration = declaration
        self.declaration_list = declaration_list

    def execute(self):
        self.declaration.execute()
        if self.declaration_list:
            self.declaration_list.execute()

class Number(Node):
    
    def __init__(self, value):
        self.type = 'NUMBER'
        self.value = value

    def execute(self):
        return self.value

class Boolean(Node):
    
    def __init__(self, value):
        self.type = 'BOOLEAN'
        self.value = value

    def execute(self):
        return True if self.value == 'true' else False

class String(Node):
    
    def __init__(self, value):
        self.type = 'STRING'
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
            print("Undefined name {}".format(self.name))
            return 0 # Maybe None

class List(Node):

    def __init__(self, item, items=None):
        self.type = 'LIST'
        self.item = item
        self.items = items
    
    def execute(self):
        if not self.items:
            if self.item == 'true' or self.item == 'false':
                return [True if self.item == 'true' else False]
            else:
                return [self.item]
        else:
            elements = self.items.split(',')[1:]
            if self.item == 'true' or self.item == 'false':
                return [True if self.item == 'true' else False] + [True if x == 'true' else False for x in elements]
            elif isinstance(self.item, int):
                return [self.item] + [int(x) for x in elements]
            else:
                return [self.item] + [x for x in elements]

class Declaration(Node):

    def __init__(self, name, value, scope):
        self.type = 'DECLARATION'
        self.name = name
        self.value = value
        self.scope = scope

    def execute(self):
        symbol_table.add_symbol(self.name, '', self.value.execute(), self.scope)

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

class ListBinaryOp(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'LIST_BINARY_OP'

    def execute(self):
        left_exec = self.left.execute()
        right_exec = self.right.execute()
        temp_list = left_exec if isinstance(left_exec, list) else right_exec
        temp_value = left_exec if not isinstance(left_exec, list) else right_exec
        if self.op == '+': return [x+temp_value for x in temp_list]
        if self.op == '-': return [x-temp_value for x in temp_list]
        if self.op == '*': return [x*temp_value for x in temp_list]
        if self.op == '/': return [x/temp_value for x in temp_list]
        else: return 0

class RelExpression(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'REL_EXPR'

    def execute(self):
        if self.op == '<': return self.left.execute() < self.right.execute()
        if self.op == '<=': return self.left.execute() <= self.right.execute()
        if self.op == '>': return self.left.execute() > self.right.execute()
        if self.op == '>=': return self.left.execute() >= self.right.execute()
        if self.op == '==': return self.left.execute() == self.right.execute()
        if self.op == '!=': return self.left.execute() != self.right.execute()
        else: return 0

class ListRelExpression(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'LIST_REL_EXPR'

    def execute(self):
        left_exec = self.left.execute()
        right_exec = self.right.execute()
        temp_list = left_exec if isinstance(left_exec, list) else right_exec
        temp_value = left_exec if not isinstance(left_exec, list) else right_exec
        if self.op == '<': return [x for x in temp_list if x < temp_value]
        if self.op == '<=': return [x for x in temp_list if x <= temp_value]
        if self.op == '>': return [x for x in temp_list if x > temp_value]
        if self.op == '<=': return [x for x in temp_list if x <= temp_value]
        if self.op == '==': return [x for x in temp_list if x == temp_value]
        if self.op == '!=': return [x for x in temp_list if x != temp_value]
        else: return 0

class UnaryRelExpression(Node):

    def __init__(self, item):
        self.type = 'UNARY_REL_EXPR'
        self.item = item

    def execute(self):
        return not self.item.execute()

class AndRelExpression(Node):

    def __init__(self, left, right):
        self.type = 'AND_REL_EXPR'
        self.left = left
        self.right = right

    def execute(self):
        return self.left.execute() and self.right.execute()

class OrRelExpression(Node):

    def __init__(self, left, right):
        self.type = 'OR_REL_EXPR'
        self.left = left
        self.right = right

    def execute(self):
        return self.left.execute() or self.right.execute()

class Input(Node):

    def __init__(self):
        self.type = 'INPUT'

    def execute(self):
        return input()

class Print(Node):

    def __init__(self, item):
        self.type = 'PRINT'
        self.item = item

    def execute(self):
        print(self.item.execute())

class LambdaReduce(Node):

    def __init__(self, id_name, op, scope):
        self.type = 'LAMBDA_REDUCE'
        self.id_name = id_name
        self.scope = scope
        self.op = op

    def execute(self):
        current_id = symbol_table.get_element(self.id_name, self.scope)
        if current_id:
            if self.op == '+': return functools.reduce(lambda x,y: x+y, current_id[1])
            if self.op == '-': return functools.reduce(lambda x,y: x-y, current_id[1])
            if self.op == '/': return functools.reduce(lambda x,y: x/y, current_id[1])
            if self.op == '*': return functools.reduce(lambda x,y: x*y, current_id[1])
        else:
            print("Undefined name {}".format(self.id_name))
            return 0

class If(Node):

    def __init__(self, condition, stmt, else_stmt=None):
        self.type = 'IF'
        self.condition = condition
        self.stmt = stmt
        self.else_stmt = else_stmt

    def execute(self):
        if self.condition.execute():
            self.stmt.execute()
        elif self.else_stmt:
            self.else_stmt.execute()

class For(Node):

    def __init__(self, id_name, items, stmt, scope):
        self.id_name = id_name
        self.items = items
        self.stmt = stmt
        self.scope = scope
        self.type = 'FOR'

    def execute(self):
        current_scope = self.scope + 1
        for x in self.items.execute():
            symbol_table.add_symbol(self.id_name, '', x, current_scope)
            self.stmt.execute()
        symbol_table.remove_element(self.id_name, current_scope)
        current_scope = self.scope - 1
