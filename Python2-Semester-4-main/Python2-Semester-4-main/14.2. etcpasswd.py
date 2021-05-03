def send(login, name):
    print(f'To: {login}\n{name}, ваш пароль слишком простой, смените его.\n')
 
 
with open("a.txt", "r") as f:
    lst = f.read().split('\n')
 
for item in lst:
    if len(item) <= 10:
        break
    dat = item.split(":")
    if dat[1] in lst[-1]:
        send(dat[0], dat[4].split(",")[0])