from enum import (
    auto,
    Enum,
    unique
)
from typing import Dict, NamedTuple


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

class  Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f"Type: {self.token_type}, Literal: {self.literal}"


class Tokens(object):
    TOKENS: Dict[str, TokenType] = {
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

    TOKENS_REGEX: Dict[TokenType, str] = {
        TokenType.ASSIGN: r'=',
        TokenType.COMMA: r',',
        TokenType.SEMICOLON: r';',
        TokenType.PLUS: r'\+',
        TokenType.LBRACE: r'{',
        TokenType.RBRACE: r'}',
        TokenType.LPARENT: r'\(',
        TokenType.RPARENT: r'\)',
        TokenType.LET: r'let',
        TokenType.FUNCTION: r'fn',
        TokenType.EOF: r'',
    }

    LETTER: str = r'^[a-zA-Z_]$'
    NUMBER: str = r'^\d$'
    WHITESPACE: str = r'^[\s\t]$'

    @classmethod
    def lookup(cls, value: str) -> bool:
        return value in cls.TOKENS
    
    @classmethod
    def lookup_token_type(cls, value: str) -> TokenType:
        
        return cls.TOKENS.get(value, TokenType.IDENT)