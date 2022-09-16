# BFS (DFS는 시간초과)
from collections import deque


case = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(graph):
    q = deque()
    # x, y, count , (이전 좌표)
    q.append((0, 0, 0, (-1, -1)))

    while q:
        x, y, count, before = q.popleft()

        # print(x, y, count, before)

        for i in range(4):
            nextX= x + dx[i]
            nextY= y + dy[i]

            # print(nextX, nextY)

            if not (0 <= nextX < n and 0 <= nextY < m):
                continue

            if nextX == n - 1 and nextY == m - 1:
                print(count + 2)
                return
            
            if (nextX != before[0] or nextY != before[1]) and graph[nextX][nextY] != 0:
                q.append((nextX, nextY, count + 1, (x, y)))


for _ in range(case):
    n, m = map(int, input().split())
    graph = []
    for __ in range(n):
        graph.append(list(map(int, list(input()))))
    solve(graph)