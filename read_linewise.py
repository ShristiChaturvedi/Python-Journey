with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
found = False

for line in lines:
    if "python" in line.lower():
        print(f"Yes, Python is present. Line no: {lineno}")
        found = True

    lineno += 1

if not found:
    print("No, Python is not present")