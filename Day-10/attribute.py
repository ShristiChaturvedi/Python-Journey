class Employee:
    a = 10   # Class attribute

obj = Employee()

print(Employee.a)
print(obj.a)

obj.a = 0

print(Employee.a)
print(obj.a)
