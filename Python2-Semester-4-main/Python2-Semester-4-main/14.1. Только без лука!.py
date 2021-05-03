a = int(input())
b = []
c = []
for i in range(a):
    b.append(input())
for j in range(len(b)):
    if 'лук' not in b[j]:
        c.append(b[j])
print(', '.join(c))