class Parser:
    def __init__(self):
        self.numbers = []
        self.operators = []
        self.oper = ['+', '-', '*', '/']
    
    def get_input(self):
        self.input_str = input(">> ")
    
    def parse(self):
        # 입력받은 텍스트를 공백으로 분리한다.
        tokens = self.input_str.split()
        
        # 숫자와 연산자를 저장할 리스트를 초기화한다.
        self.numbers.clear()
        self.operators.clear()
        
        # 각 토큰을 검사하여 숫자와 연산자를 구분하여 리스트에 저장한다.
        for token in tokens:
            if token.isdigit():
                # 숫자인 경우
                self.numbers.append(int(token))
            else:
                # 연산자인 경우
                self.operators.append(token)
        
        # 숫자와 연산자를 출력한다.
        print("Numbers:", self.numbers)
        print("Operators:", self.operators)
        
        # 저장된 숫자와 연산자를 이용하여 사칙연산을 수행한다.
        result = self.numbers[0]
        for i in range(1, len(self.numbers)):
            if self.operators[i-1] == "+":
                result += self.numbers[i]
            elif self.operators[i-1] == "-":
                result -= self.numbers[i]
            elif self.operators[i-1] == "*":
                result *= self.numbers[i]
            elif self.operators[i-1] == "/":
                result /= self.numbers[i]
        
        # 결과를 출력한다.
        print("Result:", result)

p = Parser()

while True:
    p.get_input()
    p.parse()
