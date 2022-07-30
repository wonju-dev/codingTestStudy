n = int(input())
field = []
count = {
    0: 0,
    1: 0,
}
for _ in range(n):
    field.append(list(map(int, input().split())))

def isAllSame(chunk):
    first = chunk[0][0]
    for row in range(len(chunk)):
        for col in range(len(chunk[0])):
            if first != chunk[row][col]:
                return False
    return True

def recursive(field):
    global count
    size = len(field)
    half = size // 2

    if isAllSame(field):
        count[field[0][0]] = count[field[0][0]] + 1
        return

    elif size != 1:
        chunkMap = [
            (range(0, half), range(0, half)),
            (range(0, half), range(half, half * 2)),
            (range(half, half * 2), range(0, half)),
            (range(half, half * 2), range(half, half * 2)),
        ]

        for xRange, yRange in chunkMap:
            chunk = []
            for x in xRange:
                row = []
                for y in yRange:
                    row.append(field[x][y])
                chunk.append(row)
            recursive(chunk)

recursive(field)

for num in count.values():
    print(num)