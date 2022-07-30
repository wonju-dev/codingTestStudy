import heapq

# (거리, node 번호)
graph = [
    [(2, 1), (1, 3), (5, 2)],
    [(3, 2), (2, 3)],
    [(3, 1)],
    [(3, 2), (1, 4)],
    [(1, 2), (2, 5)],
    []
]

# 0번 node에서 다른 node들 까지의 거리
INF = int(1e9)
distance = [0] + [INF] * 5

# 0번 node로 가는 비용은 0
q = [(0, 0)]

while q:
    # 가장 가까운 거리의 node를 pop
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for connection in graph[now]:
        dis, node = connection
        if distance[node] > distance[now] + dis:
            distance[node] = distance[now] + dis
            heapq.heappush(q, (distance[now] + dis, node))

print(distance)