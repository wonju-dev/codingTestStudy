n, k = map(int, input().split())
graph = [0 for _ in range(n)]

for i in range(n):
    graph[i] = int(input())

now = 0 
count = 0

while now != k and count < n:

    now = graph[now]
    count += 1

if count == n:
    print(-1)
else:
    print(count)
