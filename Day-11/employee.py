class Employee:

    salary = 100000
    increment = 50000

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.increment = value - self.salary


e = Employee()

print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 200000

print(e.salary)
print(e.increment)
print(e.salaryAfterIncrement)
