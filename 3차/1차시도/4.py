from collections import deque


def solution(n, lighthouse):
    # 데이터 초기화
    graph = [[] for _ in range(n + 1)]
    for pair in lighthouse:
        a, b = pair
        graph[a].append(b)
        graph[b].append(a)

    # 가장 많이 연결된 노드 번호
    mostConnectedNode = 1
    # 가장 많이 연결된 노드는 켰다는 가정에 기반한 초기화
    count = 1
    # 방문 여부 저장용
    visited = [False for _ in range(n+1)]
    enlighted = [False for _ in range(n+1)]

    # 가장 많이 연결된 노드 찾기
    for node in graph:
        if len(node) > len(graph[mostConnectedNode]):  # type: ignore
            mostConnectedNode = node

    # print(mostConnectedNode)

    # 가장 많이 연결된 노드와 연결된 놈들은 갈 필요 없음
    for i in range(len(graph[mostConnectedNode])): # type: ignore
        visited[graph[mostConnectedNode][i]] = True # type: ignore
    enlighted[mostConnectedNode] = True  # type: ignore

    q = deque()

    for index in range(1, len(graph)):
        if not enlighted[index]:
            q.append(index)
    # print(q)

    while q:
        node = q.popleft()

        if enlighted[node]:
            continue

        isAllEnlighted = True
        for friend in graph[node]:
            if not enlighted[friend]:
                enlighted[friend]
                isAllEnlighted = False
                q.append(friend)

        if not isAllEnlighted:
            count += 1
        enlighted[node] = True
    # print(count)

solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]])
solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]])