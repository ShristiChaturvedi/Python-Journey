sentence = input("Enter a sentence: ")
word = input("Enter the word to search: ")

if word.lower() in sentence.lower():
    print("True - Word Found")
else:
    print("False - Word Not Found")