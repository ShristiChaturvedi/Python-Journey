f = open(r"F:\My programs\Day-9\poems.txt")

data = f.read()

print(data)   

if "twinkle" in data.lower():
    print("The word Twinkle is present in the file")
else:
    print("The word Twinkle is not present in the file")

f.close()
