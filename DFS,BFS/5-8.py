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

visited = [False] * 9
stack = [1]

def dfs(index):
    print(index)
    visited[index] = True
    for node in graph[index]:
        if not visited[node]:
            dfs(node)


dfs(stack.pop())