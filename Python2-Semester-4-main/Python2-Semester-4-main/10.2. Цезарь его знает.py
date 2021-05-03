def ceasar_encode(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 32
        if number  > 1103:
            number -= 32
        return chr(number)
    return letter
 
shift = int(input())
for l in input():
    print(ceasar_encode(l, shift), end='')
