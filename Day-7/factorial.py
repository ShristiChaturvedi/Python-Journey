n = int(input("Enter the number: "))

result = 1

if n == 0 or n == 1:
    print(1)
else:
    while n > 1:
        result *= n
        n -= 1

    print(result)
