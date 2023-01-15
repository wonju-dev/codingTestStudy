n, m = map(int, input().split())
maze = []
for i in range(n):
    temp = []
    row = input()
    for j in range(m):
        temp.append(row[j])
    maze.append(temp)


def check(row, col, n, m, maze):
    if row < 0 or row == n or col < 0 or col == m:
        return False
    if maze[row][col] == "0":
        return False
    return True


row, col, count = 0, 0, 1
search_queue = [[row, col, count]]
visited_queue = []
while len(search_queue) != 0:
    row = search_queue[0][0]
    col = search_queue[0][1]
    count = search_queue[0][2]
    search_queue = search_queue[1:]
    if [row, col] in visited_queue:
        continue
    else:
        visited_queue.append([row, col])
        if check(row + 1, col, n, m, maze):
            search_queue.append([row + 1, col, count + 1])
        if check(row, col + 1, n, m, maze):
            search_queue.append([row, col + 1, count + 1])
        if check(row - 1, col, n, m, maze):
            search_queue.append([row - 1, col, count + 1])
        if check(row, col - 1, n, m, maze):
            search_queue.append([row, col - 1, count + 1])
    if row == n - 1 and col == m - 1:
        print(count)
        break