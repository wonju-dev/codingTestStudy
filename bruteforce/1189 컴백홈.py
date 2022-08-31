from collections import deque


r, c, k = map(int, input().split())

graph = []

for row in range(r):
    graph.append(list(input()))

start = [r - 1, 0]
home = [0, c - 1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0 

q = deque()
q.append((start[0], start[1], []))

while q:
    row, col, history = q.popleft()

    if 0 <= row < r and 0 <= col < c:
        # print(row, col, history)
        if row == home[0] and col == home[1]:
            if len(history) == k - 1:
                count += 1
            continue
        elif graph[row][col] != "T":
            for i in range(4):
                nextRow = row + dx[i]
                nextCol = col + dy[i]
                if str(nextRow) + str(nextCol) not in history:
                    cHistory = list(history)
                    cHistory.append(str(row) + str(col))
                    q.append((nextRow, nextCol, cHistory))
print(count)