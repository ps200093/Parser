class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text.replace(" ", "")
        self.tokens = []
        self.keywords = ['if', 'else', 'while', 'for', 'in', 'not', 'and', 'or', 'True', 'False']
        self.token_types = {
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '(': 'LPAREN',
            ')': 'RPAREN',
            '=': 'EQUALS',
            '<': 'LESS',
            '>': 'GREATER',
        }

    def tokenize(self):
        i = 0
        while i < len(self.input_text):
            c = self.input_text[i]

            if c.isspace():
                i += 1
            elif c.isalpha():
                j = i
                while j < len(self.input_text) and self.input_text[j].isalnum():
                    j += 1
                identifier = self.input_text[i:j]
                if identifier in self.keywords:
                    self.tokens.append(('KEYWORD', identifier))
                else:
                    self.tokens.append(('IDENTIFIER', identifier))
                i = j
            elif c.isdigit():
                j = i
                while j < len(self.input_text) and self.input_text[j].isdigit():
                    j += 1
                number = self.input_text[i:j]
                self.tokens.append(('NUMBER', number))
                i = j
            elif c in self.token_types:
                if c == '=' and i + 1 < len(self.input_text) and self.input_text[i + 1] == '=':
                    self.tokens.append(('EQUALS', '=='))
                    i += 2
                else:
                    self.tokens.append((self.token_types[c], c))
                    i += 1
            else:
                print('Invalid character: ' + c)
                break
        return self.tokens