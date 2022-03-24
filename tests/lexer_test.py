from typing import List
from unittest import TestCase
from lau.token import (Token, TokenType)
from lau.lexer import Lexer

class LexerTest(TestCase):

    def test_illegal(self) -> None:
        source: str = '!?@'
        lexer: Lexer = Lexer(source)

        tokens: List[Token] = []
        for i in range(len(source)):
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
        for i in range(len(source)):
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
        source = '{}(),;'
        lexer = Lexer(source)

        tokens = []
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
        source = 'let number = 5;'
        lexer = Lexer(source)

        tokens = []
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