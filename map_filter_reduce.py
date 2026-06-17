from functools import reduce

l = [1, 2, 3, 4, 5]

# MAP: Square each number
square_list = list(map(lambda x: x * x, l))
print("Squares:", square_list)

# FILTER: Keep only even numbers
even_list = list(filter(lambda x: x % 2 == 0, l))
print("Even Numbers:", even_list)

# REDUCE: Sum all numbers
total = reduce(lambda x, y: x + y, l)
print("Sum:", total)