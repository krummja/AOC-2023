from __future__ import annotations
from typing import NamedTuple, Literal
from enum import auto, Enum


class TokenType(Enum):
    EOF = auto()
    IDENTIFIER = auto()
    NUMBER = auto()


class Token(NamedTuple):
    token_type: TokenType
    value: str


class Lexer:

    def __init__(self, input_stream: str) -> None:
        self.input_stream = input_stream
        self.idx: int = 0
        self.line_num = 1
        self.char_num = 1
        self._may_continue = True

    @property
    def char(self) -> Literal[TokenType.EOF] | str:
        if len(self.input_stream) > 0:
            return self.input_stream[self.idx]
        return TokenType.EOF

    def next_token(self) -> Token:
        while self.char != TokenType.EOF and self._may_continue:
            match self.char:
                case " " | "\t":
                    self.consume()
                case "\n" | "\r":
                    self.consume()
                case _:
                    if self.char.isdigit():
                        token = self.parse_digits()
                        return token
                    elif self.char.isalpha():
                        token = self.parse_alpha()
                        return token
                    self.error()
        else:
            return Token(TokenType.EOF, "<EOF>")

    def parse_digits(self) -> Token:
        lexeme = ""
        while self.char != TokenType.EOF and self.char.isdigit():
            lexeme += self.char
            self.consume()
        return Token(TokenType.NUMBER, lexeme)

    def parse_alpha(self) -> Token:
        lexeme = ""
        while self.char != TokenType.EOF and self.char.isalnum():
            lexeme += self.char
            self.consume()
        return Token(TokenType.IDENTIFIER, lexeme)

    def consume(self) -> None:
        if self.char in ["\n", "\r"]:
            self.line_num += 1
        self.char_num += 1

        if self.idx >= len(self.input_stream):
            self._may_continue = False

        self.idx += 1


    def error(self) -> None:
        msg = f"Invalid character {self.char} at [{self.line_num}:{self.char_num}]"
        raise SyntaxError(msg)


class Parser:

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer
        self.lookahead: Token = self.lexer.next_token()
        self._output = []

    def parse(self) -> list[Token]:
        while self.lookahead.token_type != TokenType.EOF:
            value = ""
            if self.lookahead.token_type == TokenType.IDENTIFIER:
                value = str(self.match(TokenType.IDENTIFIER))
            elif self.lookahead.token_type == TokenType.NUMBER:
                value = self.match(TokenType.NUMBER)
            print(value)
            self._output.append(value)
        return self._output

    def consume(self) -> None:
        self.lookahead = self.lexer.next_token()

    def match(self, token_type: TokenType) -> Token | None:
        if self.lookahead.token_type == token_type:
            old_token = self.lookahead
            self.consume()
            return old_token
