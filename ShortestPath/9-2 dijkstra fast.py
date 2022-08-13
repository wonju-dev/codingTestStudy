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
        # 노드로 가는 비용, 현재 노드에서 갈 수 있는 노드
        dis, node = connection

        # 0번에서 connectedNode로 바로 가는 비용이, 현재 노드에서 거쳐가는 비용보다 비싸면 변경
        if distance[node] > distance[now] + dis:
            distance[node] = distance[now] + dis
            # connectedNode와 연결된 다른 노드들로 가는 방법들 중에, 현재 노드를 거쳐가는게 더 쌀 수 도 있으므로 검증
            heapq.heappush(q, (distance[now] + dis, node))

print(distance)