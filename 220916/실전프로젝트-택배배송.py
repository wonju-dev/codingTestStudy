from collections import deque
import time


INF = int(1e9)

def initGraph(graph, values):
    o, d, c = values
    graph[o][d] = c if graph[o][d] == INF else max([graph[o][d], c])
    graph[d][o] = c if graph[d][o] == INF else max([graph[d][o], c])


def solve():
    n = int(input())

    for _ in range(n):
        n, m, a, b = map(int, input().split())
        graph = [[INF] * (n + 1) for __ in range(n + 1)]
        visited = [True] + [False] * n
        visited[a] = True

        for __ in range(m):
            initGraph(graph, list(map(int, input().split())))

        q = deque()
        q.append((a, INF, visited))

        candis = []
        
        while q:
            now, weight, visit = q.popleft()
            # print(now, weight, visit)
            # time.sleep(1)

            if now == b:
                candis.append(weight)
            else:
                for next in range(1, n + 1):
                    value = graph[now][next]
                    if visit[next] or value == INF:
                        continue
                    else:
                        cVisit = list(visit)
                        cVisit[next] = True
                        if value < weight:
                            q.append((next, value, cVisit))
                        else:
                            q.append((next, weight, cVisit))
        print(sorted(candis, reverse=True)[0])

solve()