from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

q = deque([1])
visited = [False] * 9
visited[1] = True

while len(q) != 0:
    popped = q.popleft()
    print(popped)

    for node in graph[popped]:
        if not visited[node]:
            visited[node] = True
            q.append(node)