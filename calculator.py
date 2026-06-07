class Calculator:
    @staticmethod
    def greet():
        print("Hello!!!")

    def __init__(self, a):
        self.a = a

    def square(self):
        print(self.a ** 2)

    def cube(self):
        print(self.a ** 3)

    def sqrt(self):
        print(self.a ** 0.5)


number = Calculator(4)
number.greet()
number.square()
number.cube()
number.sqrt()