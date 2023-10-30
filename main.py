import design as figlet

class Calculator:
    def __init__(self):
        self.num1 = int(input("Enter the first number: "))
        self.num2 = int(input("Enter the second number: "))
        self.result = 0

    def addition(self):
        self.result = self.num1 + self.num2
        return self.result

    def subtraction(self):
        self.result = self.num1 - self.num2
        return self.result

    def division(self):
        if self.num2 == 0:
            print("Error: Division by zero")
        else:
            self.result = self.num1 / self.num2
            return self.result

    def multiplication(self):
        self.result = self.num1 * self.num2
        return self.result

if __name__ == "__main__":
    calc = Calculator()
    print('\n')
    print('''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division

    Enter your choice:
    ''')
    ch = int(input('> '))
    if ch == 1:
        print(calc.addition())
    elif ch == 2:
        print(calc.subtraction())
    elif ch == 3:
        print(calc.multiplication())
    elif ch == 4:
        print(calc.division())
    else:
        print("Option out of range")
