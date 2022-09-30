def getObstacleScore(graph, row, col):
    score = 0
    for dy in [-1, 1]:
        near = col + dy
        if 0 <= near < 5 and graph[row][near] == 1:
            score += 1
    return score


case = int(input())

while case:

    m = int(input())
    graph = []

    for _ in range(m):
        graph.append(list(map(int, input().split())))

    dp = [[0] * 5 for _ in range(m+1)]

    for row in range(m - 1, -1, -1):
        for col in range(5):
            if graph[row][col] != 1:
                if col == 0:
                    dp[row][col] = max([dp[row+1][col], dp[row+1][col+1]])
                elif col == 4:
                    dp[row][col] = max([dp[row+1][col-1], dp[row+1][col]])
                else:
                    dp[row][col] = max([dp[row+1][col-1], dp[row+1][col], dp[row+1][col+1]])
                
                dp[row][col] += graph[row][col] + getObstacleScore(graph, row, col)
            else:
                dp[row][col] = -1

    print(max(dp[0]))

    case -= 1