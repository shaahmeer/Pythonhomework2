letter = input()
text = input()
for word in text.split():
    if letter in word.lower():
        print(word)