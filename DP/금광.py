case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    graph = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(numbers[i + j * m])
        graph.append(row)

    dp = []
    for i in range(len(graph)):
        if i == 0:
            biggest = max(graph[i])
            index = graph[i].index(biggest)
            dp.append((biggest, index)) 
        else:
            beforeIndex = dp[i-1][1]
            nexts = [beforeIndex - 1, beforeIndex, beforeIndex + 1]

            biggest = 0
            index = 0
            for next in nexts:
                if 0 <= next < n:
                    if graph[i][next] > biggest:
                        biggest = graph[i][next]
                        index = next
            dp.append((biggest, index))

    summation = 0
    for i in range(m): 
        summation += dp[i][0]
    print(summation)