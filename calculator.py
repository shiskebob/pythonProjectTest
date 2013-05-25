from arithmetic import Adder

class Calculator:
    def __init__(self):
        self.adder = Adder()

    def addition(self, a, b):
        return self.adder.add(a, b)

    def subtraction(self, a, b):
        return self.adder.sub(a, b)