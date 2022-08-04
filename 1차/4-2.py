from collections import deque
from copy import deepcopy


def isSame(graph, target):
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] != target[row][col]:
                return False
    return True

def flip(graph, target):

    direction = target[0]
    number = int(target[1])

    flippedGraph = deepcopy(graph)

    if direction == "x":
        for i in range(len(graph[0])):
            flippedGraph[number][i] = 1 if flippedGraph[number][i] == 0 else 0
    else:
        for i in range(len(graph)):
            flippedGraph[i][number] = 1 if flippedGraph[i][number] == 0 else 0

    return flippedGraph

def isInLoop(accum):
    actionMap = {}
    for i in range(0, len(accum), 2):
        chunk = accum[i:i + 2]
        if actionMap.get(chunk) is not None:
            actionMap[chunk] = actionMap[chunk] + 1
        else:
            actionMap[chunk] = 1

    del actionMap['zz']

    isAllPaired = True
    for value in actionMap.values():
        if value % 2 != 0:
            isAllPaired = False
            break
    return isAllPaired

def solution(beginning, target):
    
    q = deque()
    # 현재 바둑판 모습 / 넘긴 횟수 / 이전 작업
    q.append((beginning, 0, "zz"))
    
    while q:
        graph, count, accum = q.popleft()

        # print(graph, count , accum)

        if isSame(graph, target):
            return count

        # 최초 모습이랑 동일하지 않으면 or 최초의 작업은 수행
        if not isSame(graph, beginning) or accum[len(accum) - 2:] == "zz":
            # row 뒤집기
            for row in range(len(graph)):
                if accum[len(accum) - 2:][0] == 'x' and accum[len(accum) - 2:][1] == str(row):
                    pass
                else:
                    action = "x" + str(row)
                    flipped = flip(graph, action)
                    q.append((flipped, count + 1, accum + action))
                    
            # col 뒤집기
            for col in range(len(graph[0])):
                if accum[len(accum) - 2:][0] == 'y' and accum[len(accum) - 2:][1] == str(col):
                    pass
                else:
                    action = "y" + str(col)
                    flipped = flip(graph, action)
                    q.append((flipped, count + 1, accum + action))
        elif isSame(graph, beginning) and isInLoop(accum):
            pass
        else:
            return -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))