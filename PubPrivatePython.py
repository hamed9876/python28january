



class calculation:
    
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addNumbers(self):
        return self.__addNumbers()

    def __addNumbers(self):
        return self.number1+self.number2


calc = calculation(5,8)
print(calc.addNumbers())