marks = []

for i in range(5):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

marks.sort()
print("Total marks:",sum(marks))
print("Sorted marks:", marks)