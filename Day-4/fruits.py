fruits = []

for i in range(5):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

for i in range(5):
    print(f"Fruit {i+1}: {fruits[i]}")
