from re import match
from lau.token import (Token, TokenType, Tokens)


class Lexer:

    def __init__(self, source: str) -> None:
        self._source = source
        self._character = ''
        self._read_position: int = 0
        self._position: int = 0
        self._read_character()
    
    def next_token(self) -> Token:
        self._skip_whitespace()

        if Tokens.lookup(self._character):
            token_type = Tokens.lookup_token_type(self._character)
            token = Token(token_type, self._character)

        elif self._is_letter(self._character):
            literal = self._read_identifier()
            token_type = Tokens.lookup_token_type(literal)
            return Token(token_type, literal)

        elif self._is_number(self._character):
            literal = self._read_number()
            return Token(TokenType.INT, literal)

        else:
            token = Token(TokenType.ILLEGAL, self._character)

        self._read_character()
        return token

    def _is_letter(self, value: str) -> bool:

        return bool(match(Tokens.LETTER, value))
    
    def _is_number(self, value: str) -> bool:
        return bool(match(Tokens.NUMBER, value))

    def _read_character(self) -> None:
        
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]
        
        self._position = self._read_position
        self._read_position += 1

    def _read_identifier(self) -> str:
        initial_position = self._position
        while self._is_letter(self._character):
            self._read_character()

        return self._source[initial_position:self._position]
    
    def _read_number(self) -> str:
        initial_position = self._position
        while self._is_number(self._character):
            self._read_character()

        return self._source[initial_position:self._position]

    def _skip_whitespace(self) -> None:
        while match(Tokens.WHITESPACE, self._character):
            self._read_character()