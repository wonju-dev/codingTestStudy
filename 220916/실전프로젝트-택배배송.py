INF = int(1e9)
candis = []

def dfs(now, weight, visited):
    global candis

    if now == b:
        candis.append(weight)
        return 
    else:
        for next in range(1, n + 1):
            value = graph[now][next]
            if not visited[next] and value != INF:
                cVisited = list(visited)
                cVisited[next] = True
                if value < weight:
                    dfs(next, value, cVisited)
                else:
                    dfs(next, weight, cVisited)

def initGraph(values):
    o, d, c = values
    graph[o][d] = c if graph[o][d] == INF else max([graph[o][d], c])
    graph[d][o] = c if graph[d][o] == INF else max([graph[d][o], c])


n = int(input())

for _ in range(n):
    n, m, a, b = map(int, input().split())
    graph = [[INF] * (n + 1) for __ in range(n + 1)]
    visited = [True] + [False] * n
    visited[a] = True
    
    for __ in range(m):
        initGraph(list(map(int, input().split())))
    
    dfs(a, INF, visited)    

    print(sorted(candis, reverse=True)[0])