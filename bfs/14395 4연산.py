from collections import deque


s, t = map(int, input().split())

if s == t:
    print(0)
else:
    q = deque()
    q.append([s, ""])

    dp = [False for _ in range(t)]

    while q:

        now, his = q.popleft()

        multiply = (now * now, "*")
        plus = (now * 2, "+")
        minus = (0, "-")
        divide = (1, "/")

        for value in [multiply, plus, minus, divide]:
            if value[0] < t:
                if not dp[value[0]]:
                    dp[value[0]] = his + value[1]
                    q.append((value[0], dp[value[0]]))
    print(dp)