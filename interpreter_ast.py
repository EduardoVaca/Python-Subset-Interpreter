# -------------------------------------
# COMPILERS PROJECT: AST Tree
# Carlos Eduardo Vaca Guerra
# A01207563
# -------------------------------------
import functools

class SymbolTable(object):
    """Structure for storing symbols on each scope.
    { 'ID-Scope': (Type, Value, Scope)}
    """

    def __init__(self):
        self.table = {}
        self.current_scope = 0
    
    def __str__(self):
        return str(self.table)

    def increase_scope(self):
        """Increase the scope on symbol table
        """
        self.current_scope += 1
    
    def decrese_scope(self):
        """Decrease the scope on symbol table
        """
        self.current_scope -= 1

    def add_symbol(self, id_name, symbol_type, symbol):
        """Adds a symbol to the table
        PARAMS:
        - id_name : Name of ID
        - symbol_type : Type of the symbol
        - symbol : Symbol to be stored 
        """
        self.table[id_name+'-'+str(self.current_scope)] = (symbol_type, symbol, self.current_scope)

    def get_element(self, symbol):
        """Gets and element from symbol table
        PARAMS:
        - symbol : name of symbol to be fetched
        RETURNS:
        - value if symbol found, None if not
        """
        for x in range(self.current_scope, -1, -1):
            if symbol+'-'+str(x) in self.table:
                return self.table[symbol+'-'+str(x)]
        return None

    def remove_elements_in_scope(self):
        """Deletes elements created in current scope
        """
        keys_to_delete = [k for k in self.table.keys() if '-'+str(self.current_scope) in k]
        for k in keys_to_delete:
            del self.table[k]

symbol_table = SymbolTable()

class Node(object):
    """Interface for a Node of AST
    """

    def execute(self):
        """Function to execute the stmt of the node
        """
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

    def __init__(self, name):
        self.name = name
        self.type = 'ID'        
    
    def execute(self):
        value = symbol_table.get_element(self.name)
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

    def __init__(self, name, value):
        self.type = 'DECLARATION'
        self.name = name
        self.value = value        

    def execute(self):
        symbol_table.add_symbol(self.name, '', self.value.execute())

class BinaryOp(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'BINARY_OP'

    def execute(self):
        if (isinstance(self.left, Number) or (isinstance(self.left, ID) and isinstance(self.left.execute(), int))) \
        and (isinstance(self.right, Number) or (isinstance(self.right, ID) and isinstance(self.right.execute(), int))):
            if self.op == '+': return self.left.execute() + self.right.execute()
            if self.op == '-': return self.left.execute() - self.right.execute()
            if self.op == '*': return self.left.execute() * self.right.execute()
            if self.op == '/': return self.left.execute() / self.right.execute()
            else: return 0
        else:
            print('Error: On binary operation must have ints')

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
        if isinstance(temp_value, Number) or isinstance(temp_value, int):
            if self.op == '+': return [x+temp_value for x in temp_list]
            if self.op == '-': return [x-temp_value for x in temp_list]
            if self.op == '*': return [x*temp_value for x in temp_list]
            if self.op == '/': return [x/temp_value for x in temp_list]
            else: return 0
        else:
            print('Error: On List binary operation must have list and int')

class RelExpression(Node):

    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op
        self.type = 'REL_EXPR'

    def execute(self):
        if (isinstance(self.left, Number) or isinstance(self.left, Boolean) or (isinstance(self.left, ID) and isinstance(self.left.execute(), int))) \
        and (isinstance(self.right, Number) or isinstance(self.right, Boolean) or (isinstance(self.right, ID) and isinstance(self.right.execute(), int))):
            if self.op == '<': return self.left.execute() < self.right.execute()
            if self.op == '<=': return self.left.execute() <= self.right.execute()
            if self.op == '>': return self.left.execute() > self.right.execute()
            if self.op == '>=': return self.left.execute() >= self.right.execute()
            if self.op == '==': return self.left.execute() == self.right.execute()
            if self.op == '!=': return self.left.execute() != self.right.execute()
            else: return 0
        else:
            print('Error: On Comparison operation must have bools or ints')

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
        if isinstance(temp_value, Number) or isinstance(temp_value, int):
            if self.op == '<': return [x for x in temp_list if x < temp_value]
            if self.op == '<=': return [x for x in temp_list if x <= temp_value]
            if self.op == '>': return [x for x in temp_list if x > temp_value]
            if self.op == '>=': return [x for x in temp_list if x >= temp_value]
            if self.op == '==': return [x for x in temp_list if x == temp_value]
            if self.op == '!=': return [x for x in temp_list if x != temp_value]
            else: return 0
        else:
            print('Error: On List comparison operation must have list and int')

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
        value = input()
        if value.isdigit():
            return int(value)
        elif value == 'true' or 'false':
            return True if value == 'true' else False
        else:
            return input()

class Print(Node):

    def __init__(self, item):
        self.type = 'PRINT'
        self.item = item

    def execute(self):
        print(self.item.execute())

class LambdaReduce(Node):

    def __init__(self, id_name, op):
        self.type = 'LAMBDA_REDUCE'
        self.id_name = id_name 
        self.op = op

    def execute(self):
        current_id = symbol_table.get_element(self.id_name)
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
            symbol_table.increase_scope()
            self.stmt.execute()
            symbol_table.remove_elements_in_scope()
            symbol_table.decrese_scope()
        elif self.else_stmt:
            symbol_table.increase_scope()
            self.else_stmt.execute()
            symbol_table.remove_elements_in_scope()
            symbol_table.decrese_scope()

class For(Node):

    def __init__(self, id_name, items, stmt):
        self.id_name = id_name
        self.items = items
        self.stmt = stmt        
        self.type = 'FOR'

    def execute(self):
        symbol_table.increase_scope()
        for x in self.items.execute():
            symbol_table.add_symbol(self.id_name, '', x)
            self.stmt.execute()        
        symbol_table.remove_elements_in_scope()
        symbol_table.decrese_scope()
