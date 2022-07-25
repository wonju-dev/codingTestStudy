import math

n = int(input())
d = [0] * 50001

d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4, n + 1):
    root = math.floor(math.sqrt(i))

    candidates = []
    for l in range(root, 0, -1):
        candidates.append(d[i - l ** 2])

    d[i] = min(candidates) + 1
print(d[n])