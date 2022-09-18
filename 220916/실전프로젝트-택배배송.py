from collections import deque

def getIndex(o, d):
    for i in range(len(graph[o])):
        next, _ = graph[o][i]
        if next == d:
            return i
    return -1

def initGraph(values):
    o, d, c = values

    index = getIndex(o, d)
    if index != -1:
        if graph[o][index][1] < c:
            graph[o][index][1] = c
    else:
        graph[o].append([d, c])

    index = getIndex(d, o)
    if index != -1:
        if graph[d][index][1] < c:
            graph[d][index][1] = c
    else:
        graph[d].append([o, c])        

n = int(input())

for _ in range(n):
    n, m, a, b = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    
    for __ in range(m):
        initGraph(list(map(int, input().split())))

    q = deque()
    q.append((a, int(1e9), -1))
    candis = []

    visited = [False] * 1001
    count = 0
    maxi = 0

    while q and count != len(graph[b]):
        now, weight, before = q.popleft()

        if now == b:
            if not visited[before]:
                visited[before] = True
                count += 1
                if maxi < weight:
                    maxi = weight
        else:
            for pair in graph[now]:
                next, wei = pair
                if next != before:
                    if weight > wei:
                        q.append((next, wei, now))
                    else:
                        q.append((next, weight, now))

    print(maxi)