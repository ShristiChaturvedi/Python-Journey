with open(f"F:\My programs\Day-12\Tables.txt", "w") as f:

    for i in range(2, 21):
        f.write(f"Table of {i}\n")

        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")

        f.write("\n")

print("Tables saved successfully in Tables.txt")