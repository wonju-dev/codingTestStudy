from collections import deque
from copy import deepcopy
from itertools import combinations

# 입력 데이터 초기화
n, m = map(int, input().split())
rawGraph = []
for _ in range(n):
    rawGraph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(graph, row, col):

    q = deque()
    q.append((row, col))

    while q:
        row, col = q.popleft()    
        for i in range(4):
            nextRow = row + dx[i]
            nextCol = col + dy[i]
            if 0 <= nextRow < n and 0 <= nextCol < m:
                if graph[nextRow][nextCol] == 0:
                    graph[nextRow][nextCol] = 2
                    q.append((nextRow, nextCol))
# 0 개수 세기
def getNumOfZero(graph):
    count = 0 
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                count += 1
    
    return count

# 벽 놓을 좌표 경우의 수
cordinates = []
for i in range(n):
    for j in range(m):
        if rawGraph[i][j] == 0:
            cordinates.append((i, j))

# 모든 경우에 대해 BFS 수행
largest = 0
cases = combinations(cordinates, 3)
for case in cases:
    graph = deepcopy(rawGraph)
    for cord in case:
        graph[cord[0]][cord[1]] = 1
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 2:
                bfs(graph, row, col)
    
    count = getNumOfZero(graph)
    if largest < count:
        largest = count

print(largest)