n = int(input())
coordinate = []

for i in range(n):
    coordinate.append(list(map(int, input().split())))

coordinate.sort(key=lambda x: (x[1], x[0]))

for e in coordinate:
    print(e[0], e[1])
