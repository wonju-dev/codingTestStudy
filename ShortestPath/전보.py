import heapq

# n: 도시 개수, m: 통로 개수, c: 보내는 도시
n, m, c = map(int, input().split())

# 초기화
INF = int(1e9)
graph = [[] for i in range(n + 1)]
distance = [INF for i in range(n + 1)]
distance[c] = 0

for _ in range(m):
    # x: from, y: to, z: cost
    x, y, z = map(int, input().split())
    graph[x].append([y, z])


q = [[c, 0]]
count = 0
longest = 0

while q:
    now, cost = heapq.heappop(q)

    if distance[now] > cost:
        continue

    for pair in graph[now]:
        node, dist = pair
        if distance[node] > distance[now] + dist:
            count += 1
            if longest < distance[now] + dist:
                longest = distance[now] + dist
            distance[node] = distance[now] + dist
            heapq.heappush(q, [node, distance[now] + dist])

print(count, longest)
