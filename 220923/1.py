# 모든 사다리를 검증할 필요 없음
# 도착지를 알고 있으므로, 도착지에서 거꾸로 올라가면 된다

from collections import deque


loop = int(input())

for _ in range(loop):
    n, m ,d = map(int, input().split())

    graph = []
    visited = [[False] * ((n-1) * 2 + 1) for __ in range(m)] 

    for __ in range(m):
        graph.append(list(input()))


    q = deque()
    q.append((m-1, (d-1)* 2))

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        # print(x, y)

        if x == 0:
            print(y // 2 + 1)
            break

        for i in [-1, 1]:
            nextCol = y + i

            if 0 <= nextCol <= (n - 1) * 2:
                if graph[x][nextCol] != " "  and not visited[x][nextCol]:
                    q.append((x, nextCol))
                    break
        else:
            q.append((x-1, y))