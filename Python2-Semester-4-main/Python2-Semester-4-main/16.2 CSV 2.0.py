list_of_strings = [input().split(',') for i in range(int(input('Введите число рядов таблицы: ')))]
list_of_results = []
for i in range(int(input('Введите число элементов таблицы, которые нужно будет вывести: '))):
    string_number, word_number = [int(i) for i in input().split(',')]
    list_of_results.append(list_of_strings[string_number][word_number])
for i in list_of_results:
    print(i)