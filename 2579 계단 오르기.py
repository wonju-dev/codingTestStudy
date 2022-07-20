n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

d = []
for i in range(n + 1):
    d.append([stairs[i], 0])

d[n][1] = n

for i in range(n, 1, -1):
    if d[i - 1][1] != d[i][1]:
        d[i - 1][1] = i
        d[i - 1][0] = d[i][0] + stairs[i - 1]

    d[i - 2][1] = i
    d[i - 2][0] = d[i][0] + stairs[i - 2]

print(max(d[0:2], key= lambda x : x[0])[0])