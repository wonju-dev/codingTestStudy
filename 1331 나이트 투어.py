X = ["", "", "A", "B", "C", "D", "E", "F", "", ""]
Y = ["", "", "1", "2", "3", "4", "5", "6", "", ""]
visited = [[False] * 6 for _ in range(6)]


def getNextPositions(now):
    x = X.index(now[0])
    y = Y.index(now[1])
    nextPosition = []

    if X[x - 2] != "":
        if Y[y - 1] != "":
            nextPosition.append(X[x - 2] + Y[y - 1])
        if Y[y + 1] != "":
            nextPosition.append(X[x - 2] + Y[y + 1])
    if X[x + 2] != "":
        if Y[y - 1] != "":
            nextPosition.append(X[x + 2] + Y[y - 1])
        if Y[y + 1] != "":
            nextPosition.append(X[x + 2] + Y[y + 1])
    if Y[y - 2] != "":
        if X[x - 1] != "":
            nextPosition.append(X[x - 1] + Y[y - 2])
        if X[x + 1] != "":
            nextPosition.append(X[x + 1] + Y[y - 2])
    if Y[y + 2] != "":
        if X[x - 1] != "":
            nextPosition.append(X[x - 1] + Y[y + 2])
        if X[x + 1] != "":
            nextPosition.append(X[x + 1] + Y[y + 2])

    return nextPosition
        
isAllGood = True
now = input()
nextPositions = getNextPositions(now)
startPosition = now
x = X.index(now[0]) - 2
y = Y.index(now[1]) - 2
visited[x][y] = True

for i in range(1, 36):
    now = input()

    x = X.index(now[0]) - 2
    y = Y.index(now[1]) - 2

    if not visited[x][y]:
        visited[x][y] = True
    else:
        isAllGood = False

    if now not in nextPositions:
        isAllGood = False

    nextPositions = getNextPositions(now)

    if i == 35:
        if startPosition not in nextPositions:
            isAllGood = False
    
if isAllGood:
    print("VALID")
else:
    print("INVALID")
