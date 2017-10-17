
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT STRING BOOLEAN EQ NEQ GT GE LT LE PLUS MINUS PROD DIV EQUALS LPAREN RPAREN LSQUARE RSQUARE COMA ID NUMBER COL SEMI IF ELSE FOR IN LAMBDA MAP REDUCE FILTER INPUT OUTPUTmulop    : PROD\n                | DIVterm : term mulop sumElement\n            | sumElementsumElement   : ID\n                    | NUMBER'
    
_lr_action_items = {'PROD':([0,],[2,]),'DIV':([0,],[3,]),'$end':([1,2,3,],[0,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'mulop':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> mulop","S'",1,None,None,None),
  ('mulop -> PROD','mulop',1,'p_mulop','interpreter.py',102),
  ('mulop -> DIV','mulop',1,'p_mulop','interpreter.py',103),
  ('term -> term mulop sumElement','term',3,'p_term','interpreter.py',108),
  ('term -> sumElement','term',1,'p_term','interpreter.py',109),
  ('sumElement -> ID','sumElement',1,'p_sumElement','interpreter.py',114),
  ('sumElement -> NUMBER','sumElement',1,'p_sumElement','interpreter.py',115),
]
