# fail
n, m = map(int, input().split())

ladders = []
for _ in range(n):
    ladders.append(list(map(int, input().split())))
ladders.sort(key= lambda x: x[0])

snakes = []
for _ in range(m):
    snakes.append(list(map(int, input().split())))
snakes.sort(key= lambda x: x[0])

INF = int(1e9)

dp = [0, 1, 1, 1, 1, 1, 1] + [INF for _ in range(94)]

for i in range(7, 101, 1):
    canGoWithDice = [dp[i - 6] + 1, dp[i - 5] + 1, dp[i - 4] + 1, dp[i - 3] + 1, dp[i - 2] + 1, dp[i - 1] + 1]
  
    for ladder in ladders:
        if ladder[1] == i:
            dp[i] = min(canGoWithDice + [dp[ladder[0]]])
            break
    else:
        dp[i] = min(canGoWithDice)

    for snake in snakes:
        if snake[1] == i:
            dp[i] = min([dp[i], dp[snake[0]]])
            break


print(dp[100])