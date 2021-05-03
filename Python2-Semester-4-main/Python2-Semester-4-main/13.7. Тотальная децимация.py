a = int(input())
b = []
for i in range(a):
    b.append(input())
c = int(input())
d = []
for i in range(len(b)):
    print(b[(i * c) % len(b)])
    b.remove(b[(i * c) % len(b)])
