case = int(input())

while case:
    length = int(input())
    
    dp = [[0] * 5 for _ in range(length + 1)]

    graph = []
    for _ in range(length):
        graph.append(list(map(int, input().split())))

    for row in range(length - 1, -1, -1):
        for col in range(5):
            # print(f"row={row}, col={col}, value={graph[row][col]}")
            if graph[row][col] != 1:

                dp[row][col] += graph[row][col]
                
                for dy in [-1, 1]:
                    next = col + dy
                    if 0 <= next < 5 and graph[row][next] == 1:
                        dp[row][col] += 1
                        
                if col == 0:
                    dp[row][col] += max([dp[row+1][col], dp[row+1][col+1]])
                elif col == 4:
                    dp[row][col] += max([dp[row+1][col-1], dp[row+1][col]])
                else:
                    dp[row][col] += max([dp[row+1][col-1], dp[row+1][col], dp[row+1][col+1]])
            
            else:
                dp[row][col] = -1

    print(max(dp[0]))

    case -= 1