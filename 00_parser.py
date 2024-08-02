class Parser:
    def __init__(self):
        self.numbers = []
        self.operators = []
        self.oper = ['+', '-', '*', '/']
    
    def get_input(self):
        self.input_str = input(">> ")
    
    def parse(self):
        # �Է¹��� �ؽ�Ʈ�� �������� �и��Ѵ�.
        tokens = self.input_str.split()
        
        # ���ڿ� �����ڸ� ������ ����Ʈ�� �ʱ�ȭ�Ѵ�.
        self.numbers.clear()
        self.operators.clear()
        
        # �� ��ū�� �˻��Ͽ� ���ڿ� �����ڸ� �����Ͽ� ����Ʈ�� �����Ѵ�.
        for token in tokens:
            if token.isdigit():
                # ������ ���
                self.numbers.append(int(token))
            else:
                # �������� ���
                self.operators.append(token)
        
        # ���ڿ� �����ڸ� ����Ѵ�.
        print("Numbers:", self.numbers)
        print("Operators:", self.operators)
        
        # ����� ���ڿ� �����ڸ� �̿��Ͽ� ��Ģ������ �����Ѵ�.
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
        
        # ����� ����Ѵ�.
        print("Result:", result)

p = Parser()

while True:
    p.get_input()
    p.parse()
