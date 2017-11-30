"""This module provides all the unit testing tools."""
import unittest
import interpreter


LEXER = interpreter.lexer
PARSER = interpreter.parser

class TestLexer(unittest.TestCase):
    """Class that tests all cases for my Subset Python lexer.
    Checks every token that should be allowed.
    """

    def test_one_word_comment(self):
        """Tests that one word comments is tokenized correctly.
        """
        LEXER.input('# word')
        self.checks_tokens(['COMMENT'])

    def test_one_line_comment(self):
        """Tests that a one line comment is tokenized correctly.
        """
        LEXER.input('# this is a comment')
        self.checks_tokens(['COMMENT'])

    def test_one_var_definition(self):
        """Tests that one variable definition is tokenized correctly.
        """
        LEXER.input('x = 10')
        self.checks_tokens(['ID', 'EQUALS', 'NUMBER'])

    def test_string(self):
        """Tests that a string is tokenized correctly.
        """
        LEXER.input('x = \'This is a string\'')
        self.checks_tokens(['ID', 'EQUALS', 'STRING'])

    def test_all_data_types(self):
        """Tests that all data types are tokenized correctly.
        """
        LEXER.input('x = \'This is a string\'')
        self.checks_tokens(['ID', 'EQUALS', 'STRING'])
        LEXER.input('x = 1234')
        self.checks_tokens(['ID', 'EQUALS', 'NUMBER'])
        LEXER.input('x = true')
        self.checks_tokens(['ID', 'EQUALS', 'BOOLEAN'])
        LEXER.input('x = false')
        self.checks_tokens(['ID', 'EQUALS', 'BOOLEAN'])

    def test_loop_instruction(self):
        """Tests that for loop instruction is tokenized correctly.
        """
        LEXER.input('for x in xs:')
        self.checks_tokens(['FOR', 'ID', 'IN', 'ID', 'COL'])

    def test_conditional_instruction(self):
        """Tests that conditional instruction is tokenized correctly.
        """
        LEXER.input('if x:')
        self.checks_tokens(['IF', 'ID', 'COL'])
        LEXER.input('else:')
        self.checks_tokens(['ELSE', 'COL'])

    def test_input_instruction(self):
        """Tests that input instruction is tokenized correctly.
        """
        LEXER.input('input()')
        self.checks_tokens(['INPUT', 'LPAREN', 'RPAREN'])

    def test_output_instruction(self):
        """Tests that output instruction is tokenized correctly.
        """
        LEXER.input('print(\'Hello World\')')
        self.checks_tokens(['OUTPUT', 'LPAREN', 'STRING', 'RPAREN'])

    def test_lamdbda_func(self):
        """Tests that lambda function is tokenized correctly.
        """
        LEXER.input('lambda x: x*2')
        self.checks_tokens(['LAMBDA', 'ID', 'COL', 'ID', 'PROD', 'NUMBER'])

    def test_map_func(self):
        """Tests that map function is tokenized correctly.
        """
        LEXER.input('map(lambda: x+1)')
        self.checks_tokens([
            'MAP', 'LPAREN', 'LAMBDA', 'COL', 'ID', 'PLUS',
            'NUMBER', 'RPAREN'])

    def test_filter_func(self):
        """Tests that filter function is tokenized correctly.
        """
        LEXER.input('filter(lambda: x == 2)')
        self.checks_tokens([
            'FILTER', 'LPAREN', 'LAMBDA', 'COL', 'ID', 'EQ',
            'NUMBER', 'RPAREN'])

    def tests_reduce_func(self):
        """Tests that reduce function is tokenized correctly.
        """
        LEXER.input('reduce(lambda: +, list)')
        self.checks_tokens([
            'REDUCE', 'LPAREN', 'LAMBDA', 'COL',
            'PLUS', 'COMA', 'ID', 'RPAREN'])

    # Tests that only succed on lexical analyzer phase.
    def test_var_definition_misplaced(self):
        """Tests that in the lexical analyzer phase a misplaced definition
        of a variable is accepted.
        """
        LEXER.input('=    x 120')
        self.checks_tokens(['EQUALS', 'ID', 'NUMBER'])
        LEXER.input('true x =')
        self.checks_tokens(['BOOLEAN', 'ID', 'EQUALS'])

    def test_string_wrong_place(self):
        """Tests that in the lexical analyzer phase a string in
        wrong place is accepted.
        """
        LEXER.input('for \'hi\' in list:')
        self.checks_tokens(['FOR', 'STRING', 'IN', 'ID', 'COL'])

    def test_var_wrong_place(self):
        """Tests that in the lexical analyzer phase a variable in
        wrong place is accepted.
        """
        LEXER.input('a b = 10')
        self.checks_tokens(['ID', 'ID', 'EQUALS', 'NUMBER'])

    def test_loop_wrong_grammar(self):
        """Tests that in the lexical analyzer phase a loop with
        wrong grammar is accepted.
        """
        LEXER.input('x in list for:')
        self.checks_tokens(['ID', 'IN', 'ID', 'FOR', 'COL'])

    def checks_tokens(self, correct_token_list):
        """Checks that the tokens obtained by lexer are the expected.
        PARAMS:
        correct_token_list -- list of ordered tokens that should be obtained by lexer.
        """
        for tok in correct_token_list:
            self.assertEqual(LEXER.token().type, tok)

if __name__ == '__main__':
    unittest.main()