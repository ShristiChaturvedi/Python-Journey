def game(a):
    with open(r"F:\My programs\Day-9\file.txt", "r") as f:
        data = f.read()

    highscore = int(data)

    if a > highscore:
        with open(r"F:\My programs\Day-9\file.txt", "w") as f:
            f.write(str(a))
        return a

    return highscore


a = int(input("Enter the score: "))
print("High Score:", game(a))