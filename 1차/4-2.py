from collections import deque


def isSame(graph, target):
    for row in range(len(graph)):
        join1 = "".join(graph[row])
        join2 = "".join(target[row])
        if join1 != join2:
            return False
            
    return True

def flip(graph, target):

    direction = target[0]
    number = int(target[1])

    flippedGraph = []
    for i in range(len(graph)):
        row = []
        for j in range(len(graph[i])):
            row.append(graph[i][j])
        flippedGraph.append(row)

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
    # 현재 바둑판 모습 / 넘긴 횟수 / 누적된 작업
    q.append((beginning, 0, "zz"))
    
    while q:
        graph, count, accum = q.popleft()

        # 현재 모습이랑 목표랑 같으면
        if isSame(graph, target):
            return count

        # 최초 모습이랑 동일하지 않으면 or 최초의 작업은 수행
        if not isSame(graph, beginning) or accum[len(accum) - 2:] == "zz":
            # row 뒤집기
            for row in range(len(graph)):
                # 이전에 뒤집은 row와 같으면 생략
                if accum[len(accum) - 2:][0] == 'x' and accum[len(accum) - 2:][1] == str(row):
                    pass
                # 같지 않으면 뒤집기
                else:
                    action = "x" + str(row)
                    flipped = flip(graph, action)
                    q.append((flipped, count + 1, accum + action))
                    
            # col 뒤집기
            for col in range(len(graph[0])):
                # 이전에 뒤집은 col과 같으면 생략
                if accum[len(accum) - 2:][0] == 'y' and accum[len(accum) - 2:][1] == str(col):
                    pass
                # 같지 않으면 뒤집기
                else:
                    action = "y" + str(col)
                    flipped = flip(graph, action)
                    q.append((flipped, count + 1, accum + action))
        # x0x1x0x1 같이 루프에 빠지는 경우 생략
        elif isInLoop(accum):
            pass
        # 최초 모습과 같으면 불가능
        else:
            return -1

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
""" 
x0
    x1
        x0
            x1 - l
        y0
            x0
            x1
            y1
        y1
    y0
        x0
        x1
        y1
    y1
        x0
        x1
        y0
x1
    x0
        x1                   
        y0
        y1
    y0
        x0
        x1
        y1
    y1
        x0
        x1
        y0
y1
    x0
        x1
        y0
        y1
    x1
        x0
        y0
        y1
    y0
        x0
        x1
        y1
y2
    x0
        x1
        y0
        y1
    x1
        x0
        y0
        y1
    y0
        x0
        x1
        y1 """