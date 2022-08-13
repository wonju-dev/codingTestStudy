n = int(input())
time = []

for _ in range(n):
    a,b = map(int, input().split())
    time.append((a, b))

time.sort(key = lambda x : x[0])
time.sort(key = lambda x : x[1])

endTime = time[0][1]

count = 1

for i in range(1, n):
    if time[i][0] >= endTime:
        count += 1
        endTime = time[i][1]

print(count)