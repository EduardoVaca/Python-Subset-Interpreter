import unittest
import interpreter

lexer = interpreter.lexer

class TestTry(unittest.TestCase):

    def test_try(self):
        lexer.input('hi')        
        self.assertEqual(lexer.token().type, 'ID')

if __name__ == '__main__':
    unittest.main()