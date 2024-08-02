from Lexer import Lexer
from Parser import Parser

# Test Codes
expressions = [
    "3 + 5",
    "10 - 2",
    "7 * 4",
    "8 / 2",
    "(3+5) * 2",
    "10 +    (2 * 3) - 5",
    "100 /(5 +5)",
    "2* 3  + 4"
]

for expr in expressions:
    lexer = Lexer(expr)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    result = parser.parse()
    print(f"{expr} = {result}")