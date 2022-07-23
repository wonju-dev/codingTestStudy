l = int(input())

for _ in range(l):
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4
    n = int(input())

    for i in range(4, n + 1):
        d[i] = sum([d[i-3], d[i-2], d[i-1]])

    print(d[n])