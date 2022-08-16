n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

biggest = 0

# ----
# 2가지 경우

delta = {
    1: {
        "dx" : [[0, 0, 0, 0],[0, 1, 2, 3]],
        "dy" : [[0, 1, 2, 3],[0, 0, 0, 0]]
    },
    2: {
        "dx" : [[0, 0, 1, 1]],
        "dy" : [[0, 1, 0, 1]]
    },
    3: {
        "dx": [[0, 1, 2, 2], [0, 0, 0, -1], [0, -1, -2, -2], [0, 0, 0, 1],    [0, 1, 2, 2],  [0, 0, 0, 1], [0, -1, -2, -2], [0, 0, 0, -1]],
        "dy": [[0, 0, 0, 1], [0, 1, 2, 2],  [0, 0, 0, -1],   [0, -1, -2, -2], [0, 0, 0, -1], [0, 1, 2, 2], [0, 0, 0, 1],    [0, -1, -2, -2]]
    },
    4: {
        "dx": [[0, 1, 1, 2], [0, 0, -1, -1], [0, -1, -1, -2], [0, 0, 1, 1],    [0, 1, 1 ,2],  [0, 0, 1, 1], [0, -1, -1, -2], [0, 0, -1, -1]],
        "dy": [[0, 0, 1, 1], [0, 1, 1, 2],   [0, 0, -1, -1],  [0, -1, -1, -2], [0, 0, -1, -1],[0, 1, 1, 2], [0, 0, 1, 1],    [0, -1, -1, -2]]
    },
    5: {
        "dx": [[0, 0, 0, 1],[0, -1, -2, -1],[0, 0, 0, -1],[0, -1, -2, -1]],
        "dy": [[0, 1, 2, 1],[0, 0, 0, 1],[0, 1, 2, 1],[0, 0, 0, -1]]
    }
}

def check(x, y) :
    global biggest

    for shape in delta.values():
        dx = shape['dx']
        dy = shape['dy']
        for i in range(len(dx)):
            # print(dx[i], dy[i])
            summation = 0
            for j in range(4):
                if 0 <= x + dx[i][j] <= n - 1 and 0 <= y + dy[i][j] <= m - 1:
                    # print(x + dx[i][j], y + dy[i][j])
                    summation += graph[x + dx[i][j]][y + dy[i][j]]

            if biggest < summation:
                biggest = summation
            # print()


for x in range(n):
    for y in range(m):
        check(x, y)

print(biggest)