class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __len__(self):
        return 3


# Test the implementation
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)

print("Addition:", v1 + v2)

print("Dot Product:", v1 * v2)

print("Length of vector:", len(v1))
