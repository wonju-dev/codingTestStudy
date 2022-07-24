from collections import deque

n = int(input())
p = int(input())

visited = [False] * (n + 1)
field = {}

for _ in range(p):
    f, t = map(int, input().split())

    connection = field.get(f)
    if connection is None:
        field[f] = [t]
    else:
        connection.append(t)
        field[f] = connection

    connection = field.get(t)
    if connection is None:
        field[t] = [f]
    else:
        connection.append(f)
        field[t] = connection

connection = field.get(1)
q = deque()
q.append(connection)
visited[1] = True
count = 0

while q:
    connection = q.popleft()
    print(connection)
    for node in connection:
        if not visited[node]:
            count += 1
            visited[node] = True
            nodeConnection = field.get(node)
            q.append(nodeConnection)

print(count)