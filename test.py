from collections import deque
from copy import deepcopy

def isSame(beginning, target):
    for x in range(len(beginning)):
        for y in range(len(beginning[0])):
            if beginning[x][y] != target[x][y]:
                return False

    return True

def flip(beginning, action):
    copy = deepcopy(beginning) 
    if action[0] == "x":
        row = int(action[1])
        for i in range(len(copy[row])):
            if copy[row][i] == 1:
                copy[row][i] = 0
            else:
                copy[row][i] = 1
    else:
        col = int(action[1])
        for i in range(len(copy[0])):
            if copy[i][col] == 1:
                copy[i][col] = 0
            else:
                copy[i][col] = 1
    return copy

def solution(beginning, target):
    q = deque()
    q.append([beginning, 0, "z10"])

    loop = 0

    while q:
        field, count, previousAction = q.popleft()
        if isSame(field, target):
            return count
        else:
            # row
            for i in range(len(field)):
                action = "x"+str(i)
                if previousAction[0] == "x" and i != previousAction[1:]:
                    q.append([flip(field, action), count + 1, action])
                else:
                    q.append([flip(field, action), count + 1, action])  
            # col
            for i in range(len(field[0])):
                action = "y"+str(i)
                if previousAction[0] == "y" and i != previousAction[1:]:
                    q.append([flip(field, action), count + 1, action])
                else:
                    q.append([flip(field, action), count + 1, action])  
        if loop == 3:
            break
        loop += 1
    return -1