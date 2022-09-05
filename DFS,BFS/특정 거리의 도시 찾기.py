# n: 노드 개수 / m: 간선 개수 / k: 목표값 / x: 시작 노드 번호
from collections import deque


n, m, k, x = map(int, input().split())

# 연결 정보 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((x, 0))
visited = [False] * (n + 1)
visited[x] = True

shortestNodes = []

while q:
    now, count = q.popleft()

    if count == k:
        shortestNodes.append(now)
        continue

    for node in graph[now]:
        if not visited[node]:
            visited[node] = True
            q.append((node, count + 1))

if len(shortestNodes) == 0:
    print(-1)
else:
    shortestNodes.sort()
    for i in range(len(shortestNodes)):
        print(shortestNodes[i])