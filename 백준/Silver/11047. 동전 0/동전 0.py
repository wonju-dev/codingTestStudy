import sys

n, k = map(int, sys.stdin.readline().split())
values = [0 for _ in range(n)]
count = 0
index = 0
for index in range(n):
    value = int(sys.stdin.readline())
    if value <= k:
        values[index] = value
        index += 1
    else:
        break
values = values[:index]
index = -1
while k > 0:
    if k // values[index] >= 1:
        count += k // values[index]
        k = k - values[index] * (k // values[index])
    else:
        index -= 1
print(count)