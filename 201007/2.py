case = int(input())

def getDistance(positions, row, col):
    distance = 0 
    
    for position in positions:
        if position[0] != row or position[1] != col:
            # print(position[0], position[1], row, col)
            dis = abs(row - position[0]) + abs(col - position[1])
            if dis <= 3:
                distance += 2
            if dis <= 10:
                distance += 1

    return distance


while case > 0:

    size, count = map(int, input().split())
    position = []

    for _ in range(count):
        x, y = map(int, input().split())
        position.append((x, y))

    # print(position)

    best = (-1, -1, -1)

    for row in range(size):
        for col in range(size):
            d = getDistance(position, row, col)
            # print(row, col, d)
            if d > best[2]:
                best = (row, col, d)
            elif d == best[2]:
                if best[0] > row:
                    best = (row, col, d)
                elif best[0] == row:
                    if best[1] > col:
                        best = (row, col, d)

    print(best[0], best[1], best[2])
    case -= 1