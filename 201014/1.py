testCase = int(input())

def printGraph(graph, n):
    for row in range(n):
        for col in range(n):
            print(graph[row][col], end = " ")
        print()

while testCase > 0:
    n, m = map(int, input().split())
    a, b = map(int, input().split())

    graph = [[0] * n for _ in range(n)]

    poisions = []
    heals = []

    # poision
    for _ in range(a):
        x, y = map(int, input().split())
        poisions.append([x, y])
    
    for t in range(1, m + 1):
        for p in poisions:
            # leftTop, rightTop, rightBot, leftBot
            tPoisions = [[p[0] - t, p[1] - t], [p[0] - t, p[1] + t], [p[0] + t, p[1] + t], [p[0] + t, p[1] - t]]

            for i in range(4):
                x, y = tPoisions[i]

                if x < 0:
                    tPoisions[i][0] = 0
                if y < 0:
                    tPoisions[i][1] = 0
                if x >= n:
                    tPoisions[i][0] = n - 1
                if y >= n:
                    tPoisions[i][1] = n - 1

            for row in range(tPoisions[0][0], tPoisions[2][0] + 1, 1):
                for col in range(tPoisions[0][1], tPoisions[2][1] + 1, 1):
                    # print(row, col)
                    graph[row][col] -= 1

    # heal
    for _ in range(b):
        x, y = map(int, input().split())

        heals.append([x, y])

    for t in range(1, m + 1):
        for h in heals:
            # top, right, bot, left
            points  =  [[h[0]- t , h[1]], [h[0], h[1] + t], [h[0] + t, h[1]], [h[0], h[1] - t]]

            for i in range(4):
                x, y = points[i]

                if x < 0:
                    points[i][0] = 0
                if y < 0:
                    points[i][1] = 0
                if x >= n:
                    points[i][0] = n - 1
                if y >= n:
                    points[i][1] = n - 1

            print(points)
            # 2사분면
            for row in range(points[3][0] - points[0][0]):
                for col in range(points[0][1] - points[3][1]):
                    print(row, col)
                    if abs(row - h[0]) + abs(col - h[1]) <= t:
                        graph[row][col] += 1
            # 1사분면
            # 3사분면
            # 4사분면

            print(points)



    printGraph(graph, n)

    testCase -=1
