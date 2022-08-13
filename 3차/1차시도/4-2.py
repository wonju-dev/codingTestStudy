def solution(n, lighthouse):
    INF = int(1e9)
   
    # 데이터 초기화
    graph = [[] for _ in range(n + 1)]
    for pair in lighthouse:
        a, b = pair
        graph[a].append(b)
        graph[b].append(a)


    # 가장 많이 연결된 노드 번호
    mostConnectedNode = 1
    # 가장 많이 연결된 노드 찾기
    for node in graph:
        if len(node) > len(graph[mostConnectedNode]):  # type: ignore
            mostConnectedNode = node

    visited = [False for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]

    visited[mostConnectedNode] = True
    distance[mostConnectedNode] = 0

    