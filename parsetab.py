
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT STRING OP_STRING OP_NUMBER BOOLEAN OP_BOOLEAN EQ NEQ GT GE LT LE PLUS MINUS PROD DIV EQUALS LPAREN RPAREN LSQUARE RSQUARE COMA ID OP_ID NUMBER COL SEMI IF ELSE FOR IN AND OR NOT LAMBDA MAP REDUCE FILTER INPUT OUTPUTdeclarationList  : declaration declarationList\n                        | declarationdeclaration  : varDeclaration SEMI\n                    | statementvarDeclaration   : ID EQUALS declarationElementdeclarationElement   : list\n                            | sumExpression\n                            | STRING                        \n                            | BOOLEAN\n                            | inputStmtlist   : LSQUARE listElements RSQUARElistElements : NUMBER\n                    | NUMBER OP_NUMBER\n                    | STRING\n                    | STRING OP_STRING\n                    | BOOLEAN\n                    | BOOLEAN OP_BOOLEANstatement    : expressionStmt SEMI\n                    | conditionalStmt\n                    | iterationStmt\n                    | functionalStmt SEMI\n                    | inputStmt SEMI\n                    | outputStmt SEMI\n                    | commentStmtiterationStmt    : FOR ID IN iterationElement COL declarationListiterationElement : list\n                        | IDconditionalStmt  : IF expressionStmt COL declarationList\n                        | IF expressionStmt COL declarationList ELSE COL declarationListexpressionStmt   : expressionStmt OR andExpression\n                        | andExpressionandExpression    : andExpression AND unaryRelExpression\n                        | unaryRelExpressionunaryRelExpression   : NOT unaryRelExpression\n                            | relExpressionrelExpression    : sumExpression relop sumExpression\n                        | sumExpressionrelop    : LE\n                | LT\n                | GT\n                | GE\n                | EQ\n                | NEQsumExpression    : sumExpression sumop term\n                        | termsumop    : PLUS\n                | MINUSterm : term mulop sumElement\n            | sumElementsumElement   : ID\n                    | NUMBERmulop    : PROD\n                | DIVfunctionalStmt   : FILTER LPAREN lambdaFilter RPAREN\n                        | MAP LPAREN lambdaStmt RPAREN\n                        | REDUCE LPAREN lambdaStmt RPARENlambdaStmt   : LAMBDA lambdaElement COL sumExpression COMA iterationElementlambdaElement    : ID\n                        | ID OP_IDlambdaFilter : LAMBDA lambdaElement COL expressionStmt COMA iterationElementinputStmt  : INPUT LPAREN RPARENoutputStmt : OUTPUT LPAREN declarationElement RPARENcommentStmt    : COMMENT'
    
_lr_action_items = {'ID':([0,2,4,7,8,12,14,15,21,23,29,30,31,32,33,34,35,36,37,45,47,48,49,50,51,52,53,54,55,56,57,58,59,69,70,72,74,85,101,102,104,105,106,109,110,111,],[5,5,-4,-19,-20,-24,39,40,-63,39,-1,-3,39,-18,39,-21,-22,-23,39,39,39,39,-38,-39,-40,-41,-42,-43,-46,-47,39,-52,-53,5,86,91,91,-28,5,39,39,5,-25,-29,86,86,]),'IF':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[14,14,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,14,-28,14,14,-25,-29,]),'FOR':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[15,15,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,15,-28,15,15,-25,-29,]),'FILTER':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[16,16,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,16,-28,16,16,-25,-29,]),'MAP':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[17,17,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,17,-28,17,17,-25,-29,]),'REDUCE':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[18,18,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,18,-28,18,18,-25,-29,]),'INPUT':([0,2,4,7,8,12,21,29,30,31,32,34,35,36,45,69,85,101,105,106,109,],[19,19,-4,-19,-20,-24,-63,-1,-3,19,-18,-21,-22,-23,19,19,-28,19,19,-25,-29,]),'OUTPUT':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[20,20,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,20,-28,20,20,-25,-29,]),'COMMENT':([0,2,4,7,8,12,21,29,30,32,34,35,36,69,85,101,105,106,109,],[21,21,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,21,-28,21,21,-25,-29,]),'NOT':([0,2,4,7,8,12,14,21,23,29,30,32,33,34,35,36,37,69,85,101,102,105,106,109,],[23,23,-4,-19,-20,-24,23,-63,23,-1,-3,-18,23,-21,-22,-23,23,23,-28,23,23,23,-25,-29,]),'NUMBER':([0,2,4,7,8,12,14,21,23,29,30,31,32,33,34,35,36,37,45,47,48,49,50,51,52,53,54,55,56,57,58,59,66,69,85,101,102,104,105,106,109,],[28,28,-4,-19,-20,-24,28,-63,28,-1,-3,28,-18,28,-21,-22,-23,28,28,28,28,-38,-39,-40,-41,-42,-43,-46,-47,28,-52,-53,82,28,-28,28,28,28,28,-25,-29,]),'$end':([1,2,4,7,8,12,21,29,30,32,34,35,36,85,106,109,],[0,-2,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,-28,-25,-29,]),'ELSE':([2,4,7,8,12,21,29,30,32,34,35,36,85,106,109,],[-2,-4,-19,-20,-24,-63,-1,-3,-18,-21,-22,-23,100,-25,-29,]),'SEMI':([3,5,6,9,10,11,13,22,24,25,26,27,28,39,46,60,61,62,63,64,65,67,68,76,78,79,80,89,92,94,95,96,],[30,-50,32,34,35,36,-31,-33,-35,-37,-45,-49,-51,-50,-34,-5,-6,-7,-8,-9,-10,-30,-32,-61,-36,-44,-48,-54,-55,-56,-62,-11,]),'EQUALS':([5,],[31,]),'PROD':([5,26,27,28,39,79,80,],[-50,58,-49,-51,-50,58,-48,]),'DIV':([5,26,27,28,39,79,80,],[-50,59,-49,-51,-50,59,-48,]),'LE':([5,25,26,27,28,39,79,80,],[-50,49,-45,-49,-51,-50,-44,-48,]),'LT':([5,25,26,27,28,39,79,80,],[-50,50,-45,-49,-51,-50,-44,-48,]),'GT':([5,25,26,27,28,39,79,80,],[-50,51,-45,-49,-51,-50,-44,-48,]),'GE':([5,25,26,27,28,39,79,80,],[-50,52,-45,-49,-51,-50,-44,-48,]),'EQ':([5,25,26,27,28,39,79,80,],[-50,53,-45,-49,-51,-50,-44,-48,]),'NEQ':([5,25,26,27,28,39,79,80,],[-50,54,-45,-49,-51,-50,-44,-48,]),'PLUS':([5,25,26,27,28,39,62,78,79,80,108,],[-50,55,-45,-49,-51,-50,55,55,-44,-48,55,]),'MINUS':([5,25,26,27,28,39,62,78,79,80,108,],[-50,56,-45,-49,-51,-50,56,56,-44,-48,56,]),'AND':([5,13,22,24,25,26,27,28,39,46,67,68,78,79,80,],[-50,37,-33,-35,-37,-45,-49,-51,-50,-34,37,-32,-36,-44,-48,]),'OR':([5,6,13,22,24,25,26,27,28,38,39,46,67,68,78,79,80,107,],[-50,33,-31,-33,-35,-37,-45,-49,-51,33,-50,-34,-30,-32,-36,-44,-48,33,]),'COL':([13,22,24,25,26,27,28,38,39,46,67,68,78,79,80,86,87,88,90,91,93,96,100,103,],[-31,-33,-35,-37,-45,-49,-51,69,-50,-34,-30,-32,-36,-44,-48,-27,101,-26,102,-58,104,-11,105,-59,]),'COMA':([13,22,24,25,26,27,28,39,46,67,68,78,79,80,107,108,],[-31,-33,-35,-37,-45,-49,-51,-50,-34,-30,-32,-36,-44,-48,110,111,]),'LPAREN':([16,17,18,19,20,],[41,42,43,44,45,]),'RPAREN':([26,27,28,39,44,61,62,63,64,65,71,73,75,76,77,79,80,86,88,96,112,113,],[-45,-49,-51,-50,76,-6,-7,-8,-9,-10,89,92,94,-61,95,-44,-48,-27,-26,-11,-60,-57,]),'STRING':([31,45,66,],[63,63,83,]),'BOOLEAN':([31,45,66,],[64,64,84,]),'LSQUARE':([31,45,70,110,111,],[66,66,66,66,66,]),'IN':([40,],[70,]),'LAMBDA':([41,42,43,],[72,74,74,]),'RSQUARE':([81,82,83,84,97,98,99,],[96,-12,-14,-16,-13,-15,-17,]),'OP_NUMBER':([82,],[97,]),'OP_STRING':([83,],[98,]),'OP_BOOLEAN':([84,],[99,]),'OP_ID':([91,],[103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declarationList':([0,2,69,101,105,],[1,29,85,106,109,]),'declaration':([0,2,69,101,105,],[2,2,2,2,2,]),'varDeclaration':([0,2,69,101,105,],[3,3,3,3,3,]),'statement':([0,2,69,101,105,],[4,4,4,4,4,]),'expressionStmt':([0,2,14,69,101,102,105,],[6,6,38,6,6,107,6,]),'conditionalStmt':([0,2,69,101,105,],[7,7,7,7,7,]),'iterationStmt':([0,2,69,101,105,],[8,8,8,8,8,]),'functionalStmt':([0,2,69,101,105,],[9,9,9,9,9,]),'inputStmt':([0,2,31,45,69,101,105,],[10,10,65,65,10,10,10,]),'outputStmt':([0,2,69,101,105,],[11,11,11,11,11,]),'commentStmt':([0,2,69,101,105,],[12,12,12,12,12,]),'andExpression':([0,2,14,33,69,101,102,105,],[13,13,13,67,13,13,13,13,]),'unaryRelExpression':([0,2,14,23,33,37,69,101,102,105,],[22,22,22,46,22,68,22,22,22,22,]),'relExpression':([0,2,14,23,33,37,69,101,102,105,],[24,24,24,24,24,24,24,24,24,24,]),'sumExpression':([0,2,14,23,31,33,37,45,47,69,101,102,104,105,],[25,25,25,25,62,25,25,62,78,25,25,25,108,25,]),'term':([0,2,14,23,31,33,37,45,47,48,69,101,102,104,105,],[26,26,26,26,26,26,26,26,26,79,26,26,26,26,26,]),'sumElement':([0,2,14,23,31,33,37,45,47,48,57,69,101,102,104,105,],[27,27,27,27,27,27,27,27,27,27,80,27,27,27,27,27,]),'relop':([25,],[47,]),'sumop':([25,62,78,108,],[48,48,48,48,]),'mulop':([26,79,],[57,57,]),'declarationElement':([31,45,],[60,77,]),'list':([31,45,70,110,111,],[61,61,88,88,88,]),'lambdaFilter':([41,],[71,]),'lambdaStmt':([42,43,],[73,75,]),'listElements':([66,],[81,]),'iterationElement':([70,110,111,],[87,112,113,]),'lambdaElement':([72,74,],[90,93,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declarationList","S'",1,None,None,None),
  ('declarationList -> declaration declarationList','declarationList',2,'p_declarationList','interpreter.py',163),
  ('declarationList -> declaration','declarationList',1,'p_declarationList','interpreter.py',164),
  ('declaration -> varDeclaration SEMI','declaration',2,'p_declaration','interpreter.py',169),
  ('declaration -> statement','declaration',1,'p_declaration','interpreter.py',170),
  ('varDeclaration -> ID EQUALS declarationElement','varDeclaration',3,'p_varDeclaration','interpreter.py',175),
  ('declarationElement -> list','declarationElement',1,'p_declarationElement','interpreter.py',180),
  ('declarationElement -> sumExpression','declarationElement',1,'p_declarationElement','interpreter.py',181),
  ('declarationElement -> STRING','declarationElement',1,'p_declarationElement','interpreter.py',182),
  ('declarationElement -> BOOLEAN','declarationElement',1,'p_declarationElement','interpreter.py',183),
  ('declarationElement -> inputStmt','declarationElement',1,'p_declarationElement','interpreter.py',184),
  ('list -> LSQUARE listElements RSQUARE','list',3,'p_list','interpreter.py',189),
  ('listElements -> NUMBER','listElements',1,'p_listElements','interpreter.py',194),
  ('listElements -> NUMBER OP_NUMBER','listElements',2,'p_listElements','interpreter.py',195),
  ('listElements -> STRING','listElements',1,'p_listElements','interpreter.py',196),
  ('listElements -> STRING OP_STRING','listElements',2,'p_listElements','interpreter.py',197),
  ('listElements -> BOOLEAN','listElements',1,'p_listElements','interpreter.py',198),
  ('listElements -> BOOLEAN OP_BOOLEAN','listElements',2,'p_listElements','interpreter.py',199),
  ('statement -> expressionStmt SEMI','statement',2,'p_statement','interpreter.py',216),
  ('statement -> conditionalStmt','statement',1,'p_statement','interpreter.py',217),
  ('statement -> iterationStmt','statement',1,'p_statement','interpreter.py',218),
  ('statement -> functionalStmt SEMI','statement',2,'p_statement','interpreter.py',219),
  ('statement -> inputStmt SEMI','statement',2,'p_statement','interpreter.py',220),
  ('statement -> outputStmt SEMI','statement',2,'p_statement','interpreter.py',221),
  ('statement -> commentStmt','statement',1,'p_statement','interpreter.py',222),
  ('iterationStmt -> FOR ID IN iterationElement COL declarationList','iterationStmt',6,'p_iterationStmt','interpreter.py',227),
  ('iterationElement -> list','iterationElement',1,'p_iterationElement','interpreter.py',232),
  ('iterationElement -> ID','iterationElement',1,'p_iterationElement','interpreter.py',233),
  ('conditionalStmt -> IF expressionStmt COL declarationList','conditionalStmt',4,'p_conditionalStmt','interpreter.py',238),
  ('conditionalStmt -> IF expressionStmt COL declarationList ELSE COL declarationList','conditionalStmt',7,'p_conditionalStmt','interpreter.py',239),
  ('expressionStmt -> expressionStmt OR andExpression','expressionStmt',3,'p_expressionStmt','interpreter.py',244),
  ('expressionStmt -> andExpression','expressionStmt',1,'p_expressionStmt','interpreter.py',245),
  ('andExpression -> andExpression AND unaryRelExpression','andExpression',3,'p_andExpression','interpreter.py',250),
  ('andExpression -> unaryRelExpression','andExpression',1,'p_andExpression','interpreter.py',251),
  ('unaryRelExpression -> NOT unaryRelExpression','unaryRelExpression',2,'p_unaryRelExpression','interpreter.py',256),
  ('unaryRelExpression -> relExpression','unaryRelExpression',1,'p_unaryRelExpression','interpreter.py',257),
  ('relExpression -> sumExpression relop sumExpression','relExpression',3,'p_relExpression','interpreter.py',262),
  ('relExpression -> sumExpression','relExpression',1,'p_relExpression','interpreter.py',263),
  ('relop -> LE','relop',1,'p_relop','interpreter.py',276),
  ('relop -> LT','relop',1,'p_relop','interpreter.py',277),
  ('relop -> GT','relop',1,'p_relop','interpreter.py',278),
  ('relop -> GE','relop',1,'p_relop','interpreter.py',279),
  ('relop -> EQ','relop',1,'p_relop','interpreter.py',280),
  ('relop -> NEQ','relop',1,'p_relop','interpreter.py',281),
  ('sumExpression -> sumExpression sumop term','sumExpression',3,'p_sumExpression','interpreter.py',286),
  ('sumExpression -> term','sumExpression',1,'p_sumExpression','interpreter.py',287),
  ('sumop -> PLUS','sumop',1,'p_sumop','interpreter.py',296),
  ('sumop -> MINUS','sumop',1,'p_sumop','interpreter.py',297),
  ('term -> term mulop sumElement','term',3,'p_term','interpreter.py',302),
  ('term -> sumElement','term',1,'p_term','interpreter.py',303),
  ('sumElement -> ID','sumElement',1,'p_sumElement','interpreter.py',312),
  ('sumElement -> NUMBER','sumElement',1,'p_sumElement','interpreter.py',313),
  ('mulop -> PROD','mulop',1,'p_mulop','interpreter.py',326),
  ('mulop -> DIV','mulop',1,'p_mulop','interpreter.py',327),
  ('functionalStmt -> FILTER LPAREN lambdaFilter RPAREN','functionalStmt',4,'p_functionalStmt','interpreter.py',332),
  ('functionalStmt -> MAP LPAREN lambdaStmt RPAREN','functionalStmt',4,'p_functionalStmt','interpreter.py',333),
  ('functionalStmt -> REDUCE LPAREN lambdaStmt RPAREN','functionalStmt',4,'p_functionalStmt','interpreter.py',334),
  ('lambdaStmt -> LAMBDA lambdaElement COL sumExpression COMA iterationElement','lambdaStmt',6,'p_lambdaStmt','interpreter.py',339),
  ('lambdaElement -> ID','lambdaElement',1,'p_lambdaElement','interpreter.py',343),
  ('lambdaElement -> ID OP_ID','lambdaElement',2,'p_lambdaElement','interpreter.py',344),
  ('lambdaFilter -> LAMBDA lambdaElement COL expressionStmt COMA iterationElement','lambdaFilter',6,'p_lambdaFilter','interpreter.py',349),
  ('inputStmt -> INPUT LPAREN RPAREN','inputStmt',3,'p_inputStmt','interpreter.py',354),
  ('outputStmt -> OUTPUT LPAREN declarationElement RPAREN','outputStmt',4,'p_outputStmt','interpreter.py',359),
  ('commentStmt -> COMMENT','commentStmt',1,'p_commentStmt','interpreter.py',363),
]
