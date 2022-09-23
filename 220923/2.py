# dp
loop = int(input())

for _ in range(loop):
    m = int(input())
    graph = []

    for __ in range(m):
        graph.append(list(map(int, input().split())))

    dp = [[0] * 5] * m