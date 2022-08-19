from collections import deque


n, m = map(int, input().split())
visited = [False] * 101
teleport = {}

for _ in range(n + m):
    a, b = map(int, input().split())
    teleport[a] = b

q = deque()
q.append((1, 0))

while q:
    now, count  = q.popleft()

    if now == 100:
        print(count)
        break

    for i in range(1, 7):
        next = now + i

        if next <= 100 and not visited[next]:
            if teleport.get(next) != None:
                next = teleport.get(next)

            if not visited[next]:
                q.append((next, count + 1))
                visited[next] = True