dict = {}
n = int(input())
for _ in range(n):
    x = input().split(' ')
    name = x[0]
    birthday = x[1]
    month = x[2]
    if month in dict:
        dict[month].append((name, birthday))
    else:
        dict[month] = [(name, birthday)]

months = []
n = int(input())
for _ in range(n):
    months.append(input())

for month in months:
    if month in dict:
        dict[month].sort(key=lambda day: day[1])
        days = [f'{day[0]} {day[1]}' for day in dict[month]]
        print(' '.join(days))
    else:
        print()
