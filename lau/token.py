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
    DIVISION = auto()
    EQ  = auto()
    EOF = auto()
    ELSE = auto()
    ELIF = auto()
    FUNCTION = auto()
    FALSE   = auto()
    GE = auto()
    IDENT = auto()
    ILLEGAL = auto()
    INT = auto()
    IF = auto()
    LBRACE = auto()
    LT = auto()
    LTE = auto()
    LE = auto()
    LET = auto()
    LPARENT = auto()
    MINUS = auto()
    MULTIPLICATION = auto()
    NOT = auto()
    NOT_EQUAL = auto()
    PLUS = auto()
    GT = auto()
    GTE = auto()
    RBRACE = auto()
    RPARENT = auto()
    RETURN = auto()
    SEMICOLON = auto()
    TRUE = auto()

class  Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f"Type: {self.token_type}, Literal: {self.literal}"


class Tokens(object):
    TOKENS: Dict[str, TokenType] = {
        # operators.
        '=': TokenType.ASSIGN,
        '==': TokenType.EQ,
        '!=': TokenType.NOT_EQUAL,
        ',': TokenType.COMMA,
        '!': TokenType.NOT,
        ';': TokenType.SEMICOLON,
        '+': TokenType.PLUS,
        '*': TokenType.MULTIPLICATION,
        '/': TokenType.DIVISION,
        '-': TokenType.MINUS,
        '{': TokenType.LBRACE,
        '}': TokenType.RBRACE,
        '(': TokenType.LPARENT,
        ')': TokenType.RPARENT,
        '>': TokenType.GT,
        '<': TokenType.LT,
        '>=': TokenType.GTE,
        '<=': TokenType.LTE,
        '': TokenType.EOF,
        # keywords
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'elif': TokenType.ELIF,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'return': TokenType.RETURN,
        'let': TokenType.LET,
        'fn': TokenType.FUNCTION,

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
    WHITESPACE: str = r'^[\s\t\n]$'

    @classmethod
    def lookup(cls, value: str) -> bool:
        return value in cls.TOKENS
    
    @classmethod
    def lookup_token_type(cls, value: str) -> TokenType:
        return cls.TOKENS.get(value, TokenType.IDENT)