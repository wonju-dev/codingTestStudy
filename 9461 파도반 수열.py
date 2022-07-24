l = int(input())

for q in range(l):
    d = [0] * 101
    d[1] = 1
    d[2] = 1
    d[3] = 1
    n = int(input())

    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2]

    print(d[n])
