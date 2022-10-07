from collections import deque


case = int(input())

while case > 0:
    width, height, destination = map(int, input().split())
    width = width * 2 - 1

    graph = []

    for _ in range(height):
        graph.append(list(input()))

    q = deque()
    q.append((height - 1, (destination - 1) * 2, (-1, -1)))

    starts = []

    while q:
        row, col, previous = q.popleft()
        print(row, col, previous)

        if row == 0:
            print("finish", row, col, previous)
            starts.append(str(col / 2 + 1))
        else:
            for d in [-1, 1]:
                nextCol = col + d
                if 0 <= nextCol < width and (row != previous[0] or nextCol != previous[1]):
                    if graph[row][nextCol] == "+":
                        q.append((row, nextCol, (row, col)))
                        break
                    elif graph[row][nextCol] == "?":
                        if notCross(row, col):
                            q.append((row, nextCol, (row, col)))
                        if graph[row-1][col] != "0":
                            q.append((row - 1, col, (row, col)))
                        break
            else:
                q.append((row - 1, col, (row, col)))

    print(" ".join(sorted(starts)))

    case -=1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def notCross(row, col):
    for i in range(4):
        x = row + dx[i]
        y = col + dy[i]
        if 0 <= x < height and 0 <= 0 < width - 1:
            if graph[x][y] == 0:
                return False

    return True
