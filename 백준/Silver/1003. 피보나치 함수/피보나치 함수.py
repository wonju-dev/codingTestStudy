loop = int(input())


for _ in range(loop):
    d = []
    for i in range(41):
        d.append([0, 0])
    d[0][0] = 1
    d[1][1] = 1
    n = int(input())

    for i in range(2, n+1):
        d[i][0] = d[i - 1][0] + d[i - 2][0]
        d[i][1] = d[i - 1][1] + d[i - 2][1]

    print(d[n][0], d[n][1])
