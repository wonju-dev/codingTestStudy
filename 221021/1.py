from collections import deque


testCase = int(input())

movements = [
    ("F", "F", "F"),
    ("F", "R", "R"),
    ("F", "L", "L"),
    ("F", "B", "B"),
    ("R", "F", "R"),
    ("R", "R", "B"),
    ("R", "L", "F"),
    ("R", "B", "L"),
    ("L", "F", "L"),
    ("L", "R", "F"),
    ("L", "L", "B"),
    ("L", "B", "R"),
    ("B", "F", "B"),
    ("B", "R", "L"),
    ("B", "L", "R"),
    ("B", "B", "F")
]

def hasTrasure(movements):
    movementMap = {
        "F" : 0,
        "R" : 0,
        "L" : 0,
        "B" : 0
    }

    for movement in movements:
        if movementMap[movement] >= 2:
            return True
        
        movementMap[movement] += 1
    
    return False

def solve(n):
    graph = []
    graph_actions = []

    for _ in range(n):
        graph.append(input().split())
        graph_actions.append([[] for __ in range(n)])
    
    q = deque()
    q.append((0, 0, "B"))

    while q:

        x, y, beforeMovement = q.popleft()

        if hasTrasure(graph_actions[x][y]):
            print(x, y)
            return
        
        for movement in movements:
            movement_before, movement_now, movement_next = movement

            if graph[x][y][0] == movement_now and beforeMovement == movement_before:
                graph_actions[x][y].append(movement_next)
                
                if hasTrasure(graph_actions[x][y]):
                    print(x, y)
                    return
                
                if movement_next == "F":
                    q.append((x + int(graph[x][y][1]), y, "F"))
                elif movement_next == "R":
                    q.append((x, y + int(graph[x][y][1]), "R"))
                elif movement_next == "L":
                    q.append((x, y - int(graph[x][y][1]), "L"))
                elif movement_next == "B":
                    q.append((x - int(graph[x][y][1]), y, "B"))


while testCase > 0:
    n = int(input())

    solve(n)

    testCase -= 1


