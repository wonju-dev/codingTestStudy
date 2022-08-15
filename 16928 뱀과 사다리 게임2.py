from collections import deque


n, m = map(int, input().split())

ladders = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

snakes = {}
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

q = deque()
q.append((1))

visited = [0 for _ in range(101)]

while q:
    now = q.popleft()

    if now == 100:
        print(visited[now])
        break


    for i in range(1, 7):
        nextNumber = now + i
        visited[nextNumber] = visited[now] + 1

        if nextNumber <= 100 and visited[nextNumber] == 0:
            if nextNumber in ladders.keys():
                q.append(ladders[nextNumber])
            elif nextNumber in snakes.keys():
                q.append(snakes[nextNumber])
            else:
                q.append(nextNumber)