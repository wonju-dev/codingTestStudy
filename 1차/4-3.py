from collections import deque


def isSame(graph, target):
    for row in range(len(graph)):
        row1 = list(map(str, graph[row]))
        join1 = "".join(row1)

        row2 = list(map(str, target[row]))
        join2 = "".join(row2)
        if join1 != join2:
            return False
            
    return True

def rowFlip(graph, index):
    flippedGraph = []
    for i in range(len(graph)):
        row = []
        if i != index :
            for j in range(len(graph[i])):
                row.append(graph[i][j])
        else:
            for j in range(len(graph[i])):
                row.append(1 if graph[i][j] == 0 else 0)
        flippedGraph.append(row)
    return flippedGraph

def colFlip(graph, index):
    flippedGraph = []
    for i in range(len(graph)):
        row = []
        for j in range(len(graph[i])):
            if j != index:
                row.append(graph[i][j])
            else:
                row.append(1 if graph[i][j] == 0 else 0)
        flippedGraph.append(row)
    return flippedGraph

def isInLoop(accum):
    actionMap = {}
    accum = accum[2:]
    for i in range(0, len(accum), 2):
        chunk = accum[i:i + 2]
        if actionMap.get(chunk) is not None:
            actionMap[chunk] = actionMap[chunk] + 1
        else:
            actionMap[chunk] = 1

    isAllPaired = True
    for value in actionMap.values():
        if value % 2 != 0:
            isAllPaired = False
            break
    
    return isAllPaired


def solution(beginning, target):
    
    q = deque()
    q.append((beginning, 0, "zz"))
    
    while q:
        graph, count, accum = q.popleft()
        # print(graph, count, accum)

        if isSame(graph, target):
            return count

        if isSame(graph, beginning) and not isInLoop(accum):
            return -1

        else:
            # row 뒤집기
            for row in range(len(graph)):
                flipped = rowFlip(graph, row)
                q.append((flipped, count + 1, accum + "x" + str(row)))
            
            # col 뒤집기
            for col in range(len(graph[0])):
                flipped = colFlip(graph, col)
                q.append((flipped, count + 1, accum + "y" + str(col)))


    return -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
