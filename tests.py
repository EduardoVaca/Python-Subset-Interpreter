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
    
    def checks_tokens(self, correct_token_list):
        """Checks that the tokens obtained by lexer are the expected.
        PARAMS:
        correct_token_list -- list of ordered tokens that should be obtained by lexer.
        """
        for tok in correct_token_list:
            self.assertEqual(LEXER.token().type, tok)

if __name__ == '__main__':
    unittest.main()