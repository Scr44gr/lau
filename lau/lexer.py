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
        token_type = Tokens.exists(self._character)
        token = Token(token_type, self._character)
        self._read_character()
        return token

    def _read_character(self) -> None:
        
        if self._read_position >= len(self._source):
            self._character = ''
        else:
            self._character = self._source[self._read_position]
        
        self._position = self._read_position
        self._read_position += 1