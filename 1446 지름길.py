from collections import deque


n, d = map(int, input().split())

# 초기화
graph = []
for i in range(101):
    graph.append([(i + 1, 1)])

for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b, c))

# 현 위치, 비용
q = deque([(0, 0)])

print(graph)

costs = []
while q:
    now, cost = q.popleft()
    print(f"now={now}, cost={cost}")

    if now == d:
        costs.append(cost)
        continue

    for next in graph[now]:
        q.append((next[0], cost + next[1]))

print(sorted(costs)[0])