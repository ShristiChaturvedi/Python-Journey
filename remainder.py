import pyttsx3

a = int(input("Enter number 1 here: "))
b = int(input("Enter number 2 here: "))

remainder = a % b

print("Remainder of the number is:", remainder)

engine = pyttsx3.init()

engine.say(f"Remainder of the number is {remainder}")

engine.runAndWait()