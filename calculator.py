from sly import Lexer, Parser


class CalcLexer(Lexer):
    tokens = {NUMBER, PLUS, TIMES, LPAREN, RPAREN}
    ignore = " \t"

    # Tokens
    NUMBER = r"\d+"
    PLUS = r"\+"
    TIMES = r"\*"
    LPAREN = r"\("
    RPAREN = r"\)"


class CalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.precedence = {
            "PLUS": 1,
            "TIMES": 2,
        }
        self.result = 0

    @_("expr")
    def statement(self, p):
        self.result = p.expr
        return self.result

    @_("expr PLUS expr")
    def expr(self, p):
        return p.expr0 + p.expr1

    @_("expr TIMES expr")
    def expr(self, p):
        return p.expr0 * p.expr1

    @_("LPAREN expr RPAREN")
    def expr(self, p):
        return p.expr

    @_("NUMBER")
    def expr(self, p):
        return int(p.NUMBER)

    def error(self, p):
        if p:
            raise SyntaxError("Syntax error at token", p.type)
        else:
            raise SyntaxError("Syntax error at EOF")
