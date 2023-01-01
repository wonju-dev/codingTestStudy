from collections import deque

n, m = map(int, input().split())
visited = [0 for _ in range(100001)]
queue = deque()
queue.append((n, 0))

while queue:
    n, count = queue.popleft()
    if n == m:
        print(count)
        break
    for i in (n-1, n+1, 2*n):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = 1
            queue.append((i, count + 1))