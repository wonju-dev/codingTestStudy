n = int(input())
fieldForNormal = []
fieldForProblem = []
visited1 = []
visited2 = []


def replace(char):
    return "G" if char == "R" else char


for _ in range(n):
    row = list(input())
    fieldForNormal.append(row)
    fieldForProblem.append(list(map(replace, row)))
    visited1.append([False for _ in range(len(row))])
    visited2.append([False for _ in range(len(row))])

fields = [fieldForNormal, fieldForProblem]
visits = [visited1, visited2]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

stack = []

for index in range(2):
    count = 0
    for a in range(n):
        for b in range(n):
            if not visits[index][a][b]:
                stack.append((a, b))
                while len(stack) != 0:
                    x, y = stack.pop()
                    visits[index][x][y] = True

                    for i in range(4):
                        nextX = x + dx[i]
                        nextY = y + dy[i]
                        if (
                            nextX < 0
                            or nextX >= len(fields[index])
                            or nextY < 0
                            or nextY >= len(fields[index])
                        ):
                            continue
                        if (
                            not visits[index][nextX][nextY]
                            and fields[index][nextX][nextY] == fields[index][x][y]
                        ):
                            stack.append((nextX, nextY))

                count += 1
    print(count)
