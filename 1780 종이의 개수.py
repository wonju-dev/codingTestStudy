n = int(input())
field = []
count = {
    -1: 0,
    0: 0,
    1: 0,
}

for _ in range(n):
    field.append(list(map(int, input().split())))

def isAllSame(field):
    firstOne = field[0][0]
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] != firstOne:
                return False
    return True

def recursive(field):
    global count

    if isAllSame(field):
        count[field[0][0]] = count[field[0][0]] + 1
        return

    elif len(field) != 1:
        chunkSize = len(field) // 3
        chunkMap = [
            (range(0, chunkSize), range(0, chunkSize)),
            (range(0, chunkSize), range(chunkSize, chunkSize * 2)),
            (range(0, chunkSize), range(chunkSize * 2 , chunkSize * 3)),
            (range(chunkSize, chunkSize * 2), range(0, chunkSize)),
            (range(chunkSize, chunkSize * 2), range(chunkSize, chunkSize * 2)),
            (range(chunkSize, chunkSize * 2), range(chunkSize * 2 , chunkSize * 3)),
            (range(chunkSize * 2, chunkSize * 3), range(0, chunkSize)),
            (range(chunkSize * 2, chunkSize * 3), range(chunkSize, chunkSize * 2)),
            (range(chunkSize * 2, chunkSize * 3), range(chunkSize * 2 , chunkSize * 3)),
        ]

        for xChunk, yChunk in chunkMap:
            chunkField = []
            for x in xChunk:
                row = []
                for y in yChunk:
                    row.append(field[x][y])
                chunkField.append(row)
            recursive(chunkField)

recursive(field)

for num in count.values():
    print(num)