num = int(input())
first = [int(input()) for i in range(num)]
second = first
training = int(input())
for i in range(training):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input()) 
    elif brother == 2:
        second[int(input())] += int(input()) 
print(*first)
print(*second)