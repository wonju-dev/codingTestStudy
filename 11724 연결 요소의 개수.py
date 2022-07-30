from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


q = deque([0])
count = 0 

for i in range(n):
    if not visited[i]:
        visited[i] = True 
        for n in graph[i]:
            q.append(n)
        while len(q) != 0:
            popped = q.popleft()
            if not visited[popped]:
                visited[popped] = True 
                for n in graph[popped]:
                    q.append(n)
        count += 1

print(count)