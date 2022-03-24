from enum import (
    auto,
    Enum,
    unique
)
from typing import NamedTuple


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()
    FUNCTION = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPARENT = auto()
    PLUS = auto()
    RBRACE = auto()
    RPARENT = auto()
    SEMICOLON = auto()


class Tokens(object):
    TOKENS = {
        '=': TokenType.ASSIGN,
        ',': TokenType.COMMA,
        ';': TokenType.SEMICOLON,
        '+': TokenType.PLUS,
        '{': TokenType.LBRACE,
        '}': TokenType.RBRACE,
        '(': TokenType.LPARENT,
        ')': TokenType.RPARENT,
        'let': TokenType.LET,
        'fn': TokenType.FUNCTION,
        '': TokenType.EOF,
    }

    @classmethod
    def exists(cls, value: str) -> TokenType:

        if value in cls.TOKENS:
            return cls.TOKENS[value]
        
        return TokenType.ILLEGAL

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f"Type: {self.token_type}, Literal: {self.literal}"