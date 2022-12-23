from collections import deque

n, m, s = map(int, input().split())
graph = [[] * i for i in range(n + 1)]
for i in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
for i in range(1, n + 1):
    graph[i].sort()
visited = [False] * (n + 1)

answer = []


def dfs(answer, graph, s, visited):
    answer.append(str(s))
    visited[s] = True
    for node in graph[s]:
        if visited[node] == False:
            dfs(answer, graph, node, visited)


dfs(answer, graph, s, visited)
print(" ".join(answer))
visited = [False] * (n + 1)
answer = []


def bfs(answer, graph, s, visited):
    queue = deque()
    queue.append(s)
    while len(queue) != 0:
        target = queue.popleft()
        answer.append(str(target))
        visited[target] = True
        for node in graph[target]:
            if node not in queue and visited[node] == False:
                queue.append(node)


bfs(answer, graph, s, visited)
print(" ".join(answer))