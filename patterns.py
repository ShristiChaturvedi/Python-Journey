for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
print("--------")
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("--------")
for i in range(4):
    for j in range(4):
        if i==0 or i==3 or j==0 or j==3:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("--------")
for i in range(5):
    # Print spaces
    for j in range(5 - i - 1):
        print(" ", end=" ")

    # Print stars
    for j in range(2 * i + 1):
        print("*", end=" ")

    print()