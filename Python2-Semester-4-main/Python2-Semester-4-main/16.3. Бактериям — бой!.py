n = int(input('Введите размер квадратного поля: '))
number_of_bacteria = [([0] * n) for i in range(n)]
for i in range(n):
    for j in range(n):
        number_of_bacteria[i][j] = int(input())
for i in range(int(input('Введите количество капель антибиотика: '))):
    row = int(input())
    column = int(input())
    if number_of_bacteria[column][row] >= 8:
        number_of_bacteria[column][row] -= 8
    else:
        number_of_bacteria[column][row] = 0
    if column > 0:
        if number_of_bacteria[column - 1][row] >= 4:
            number_of_bacteria[column - 1][row] -= 4
        else:
            number_of_bacteria[column - 1][row] = 0
        if row > 0:
            if number_of_bacteria[column - 1][row - 1] >= 4:
                number_of_bacteria[column - 1][row - 1] -= 4
            else:
                number_of_bacteria[column - 1][row - 1] = 0
        if row < (n - 1):
            if number_of_bacteria[column - 1][row + 1] >= 4:
                number_of_bacteria[column - 1][row + 1] -= 4
            else:
                number_of_bacteria[column - 1][row + 1] = 0
    if column < (n - 1):
        if number_of_bacteria[column + 1][row] >= 4:
            number_of_bacteria[column + 1][row] -= 4
        else:
            number_of_bacteria[column + 1][row] = 0
        if row > 0:
            if number_of_bacteria[column + 1][row - 1] >= 4:
                number_of_bacteria[column + 1][row - 1] -= 4
            else:
                number_of_bacteria[column + 1][row - 1] = 0
        if row < (n - 1):
            if number_of_bacteria[column + 1][row + 1] >= 4:
                number_of_bacteria[column + 1][row + 1] -= 4
            else:
                number_of_bacteria[column + 1][row + 1] = 0
    if row > 0:
        if number_of_bacteria[column][row - 1] >= 4:
            number_of_bacteria[column][row - 1] -= 4
        else:
            number_of_bacteria[column][row - 1] = 0
    if row < n - 1:
        if number_of_bacteria[column][row + 1] >= 4:
            number_of_bacteria[column][row + 1] -= 4
        else:
            number_of_bacteria[column][row + 1] = 0
for i in range(n):
    for j in range(n):
        print(number_of_bacteria[i][j], end=' ')
    print()