import sys
sys.setrecursionlimit(2503)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(field, x, y):
    if x < 0 or x >= len(field) or y < 0 or y >= len(field[0]):
        return

    if field[x][y] == 1:
        field[x][y] = 0
        for i in range(4):
            bfs(field, x + dx[i], y + dy[i])
    else:
        return


case = int(input())
for _ in range(case):
    row, col, num = list(map(int, input().split()))
    row, col = col, row
    count = 0

    field = [[0 for _ in range(col)] for _ in range(row)]

    for _ in range(num):
        x, y = list(map(int, input().split()))
        x, y = y, x
        field[x][y] = 1

    for x in range(row):
        for y in range(col):
            if field[x][y] == 1:
                bfs(field, x, y)
                count += 1
    print(count)
