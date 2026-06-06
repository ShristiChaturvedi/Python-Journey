marks = []

for i in range(4):
    mark = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(mark)

i = 0

while i < 4:
    if marks[i] > marks[0]:
        marks[0] = marks[i]
    i += 1

print("Highest marks:", marks[0])
