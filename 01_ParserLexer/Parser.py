class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        result = self.expr()
        if self.pos != len(self.tokens):
            print("ERROR")
        return result

    def expr(self):
        left = self.bexp()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in {"AND", "OR", "NOT"}:
            op = self.tokens[self.pos][1]
            self.pos += 1
            right = self.bexp()
            if op == "&":
                return left and right
            elif op == "|":
                return left or right
            elif op == "!":
                return not left
        return left

    def bexp(self):
        left = self.aexp()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in {"EQUALS", "LESS", "GREATER"}:
            op = self.tokens[self.pos][1]
            self.pos += 1
            right = self.aexp()
            if op == "=":
                return left == right
            elif op == ">":
                return left > right
            elif op == "<":
                return left < right
        return left

    def aexp(self):
        left = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in {"PLUS", "MINUS"}:
            op = self.tokens[self.pos][1]
            self.pos += 1
            right = self.term()
            if op == "+":
                left += right
            else:
                left -= right
        return left

    def term(self):
        left = self.factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in {"MULTIPLY", "DIVIDE"}:
            op = self.tokens[self.pos][1]
            self.pos += 1
            right = self.factor()
            if op == "*":
                left *= right
            else:
                left /= right
        return left

    def factor(self):
        if self.tokens[self.pos][0] == 'NUMBER':
            val = int(self.tokens[self.pos][1])
            self.pos += 1
            return val
        elif self.tokens[self.pos][0] == 'LPAREN':
            self.pos += 1
            result = self.expr()
            if self.tokens[self.pos][0] != 'RPAREN':
                print("ERROR")
            self.pos += 1
            return result
        else:
            print("ERROR")