"""This module provides all the unit testing tools."""
import unittest
import interpreter


LEXER = interpreter.lexer

class TestLexer(unittest.TestCase):
    """Class that tests all cases for my Subset Python lexer.
    Checks every token that should be allowed.
    """

    def test_one_word_comment(self):
        """Tests that one word comments is tokenized correctly.
        """
        LEXER.input('# word')
        self.checks_tokens(['COMMENT', 'ID'])

    def test_one_line_comment(self):
        """Tests that a one line comment is tokenized correctly.
        """
        LEXER.input('# this is a comment')
        self.checks_tokens(['COMMENT', 'ID', 'ID', 'ID', 'ID'])

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

    def checks_tokens(self, correct_token_list):
        """Checks that the tokens obtained by lexer are the expected.
        PARAMS:
        correct_token_list -- list of ordered tokens that should be obtained by lexer.
        """
        for tok in correct_token_list:
            self.assertEqual(LEXER.token().type, tok)

if __name__ == '__main__':
    unittest.main()