p = [0] * 3000
a = input()
m = 0
n = len(a) - 1
s = 0
rt = True
for i in range(n):
    if i + s == n:
    break
    elif a[i + s] == '>':
        m += 1
    if m == 3000:
    m = 0
    elif a[i + s] == '<':
    m -= 1
    if m < 0:
    m = 2999
    elif a[i + s] == '+':
    p[m] = p[m] + 1
    if p[m] > 255:
    p[m] == 0
    elif a[i + s] == '-':
    p[m] -= 1
    if p[m] < 0:
    p[m] = 255
    elif a[i + s] == '.':
    print(p[m])
    elif a[i + s] == '[':
    while rt:
    if a[i + s] == ']':
    s = 0
    if p[m] == 0:
    rt = False
    else:
    continue
    else:
    s += 1
    if a[i + s] == '>':
    m += 1
    if m == 3000:
    m = 0
    elif a[i + s] == '<':
    m -= 1
    if m < 0:
    m = 2999
    elif a[i + s] == '+':
    p[m] = p[m] + 1
    if p[m] > 255:
    p[m] == 0
    elif a[i + s] == '-':
    p[m] -= 1
    if p[m] < 0:
    p[m] = 255
    elif a[i + s] == '.':
    print(p[m])
    if a[i + s + 1] == ']':
    if p[m] == 0:
    rt = False
