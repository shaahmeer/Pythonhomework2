string = input()
cout = 1
for i in range(len(string)):
    if i <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
        else:
            a = string[i]
            print(cout, string[i])
            cout = 1