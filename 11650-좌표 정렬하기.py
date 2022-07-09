n = int(input())

cords = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    cords.append((x, y))

cords.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(cords[i][0], cords[i][1])
