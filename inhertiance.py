class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector i: {self.i}, j: {self.j}")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector i: {self.i}, j: {self.j} and k: {self.k}")

num1=TwoDVector(40,70)
num1.show()

num2 = ThreeDVector(40, 67, 76)
num2.show()