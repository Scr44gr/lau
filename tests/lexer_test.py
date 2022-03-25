from typing import List
from unittest import TestCase
from lau.token import (Token, TokenType)
from lau.lexer import Lexer

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '!?@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ILLEGAL, '!'),
            Token(TokenType.ILLEGAL, '?'),
            Token(TokenType.ILLEGAL, '@')
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_one_character_operator(self) -> None:
        source: str = '=+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.PLUS, '+'),
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_eof(self) -> None:
        source: str = '+'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source) + 1):
            tokens.append(lexer.next_token())
        
        expected_tokens: List[Token] = [
            Token(TokenType.PLUS, '+'),
            Token(TokenType.EOF, '')
        ]

        self.assertEqual(tokens, expected_tokens)
    
    def test_delimiters(self):
        source: str = '{}(),;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(len(source)):
            tokens.append(lexer.next_token())
        
        expected_tokens = [
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.RBRACE, '}'),
            Token(TokenType.LPARENT, '('),
            Token(TokenType.RPARENT, ')'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.SEMICOLON, ';'),
        ]
        self.assertEqual(tokens, expected_tokens)
    
    def test_identifier(self):
        source: str = 'let number = 5;'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(5):
            tokens.append(lexer.next_token())

        expected_tokens = [
            Token(TokenType.LET, 'let'),
            Token(TokenType.IDENT, 'number'),
            Token(TokenType.ASSIGN, '='),
            Token(TokenType.INT, '5'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        self.assertEqual(tokens, expected_tokens)
    
    def test_function_declaration(self):
        source: str = 'fn add(x, y) { x + y }'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(12):
            tokens.append(lexer.next_token())
        
        expected_tokens = [
            Token(TokenType.FUNCTION, 'fn'),
            Token(TokenType.IDENT, 'add'),
            Token(TokenType.LPARENT, '('),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RPARENT, ')'),
            Token(TokenType.LBRACE, '{'),
            Token(TokenType.IDENT, 'x'),
            Token(TokenType.PLUS, '+'),
            Token(TokenType.IDENT, 'y'),
            Token(TokenType.RBRACE, '}'),
        ]
        self.assertEqual(tokens, expected_tokens)
    
    def test_function_call(self):
        source: str = 'add(5, 10);'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for _ in range(7):
            tokens.append(lexer.next_token())
        
        expected_tokens = [
            Token(TokenType.IDENT, 'add'),
            Token(TokenType.LPARENT, '('),
            Token(TokenType.INT, '5'),
            Token(TokenType.COMMA, ','),
            Token(TokenType.INT, '10'),
            Token(TokenType.RPARENT, ')'),
            Token(TokenType.SEMICOLON, ';'),
        ]
        self.assertEqual(tokens, expected_tokens)