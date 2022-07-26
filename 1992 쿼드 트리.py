n = int(input())
field = []
string = ""
for _ in range(n):
    field.append(list(map(int, list(input()))))


def isAllSame(field):
    first = field[0][0]
    for row in range(len(field)):
        for col in range(len(field[0])):
            if field[row][col] != first:
                return False
    return True

def recursive(field):
    size = len(field)
    half = size // 2
    global string

    if isAllSame(field):
        string += str(field[0][0])

    elif size == 2:
        string += "("
        for row in range(2):
            for col in range(2):
                string += str(field[row][col])
        string += ")"

    else:
        chunkMap = [
            [range(half), range(half)],
            [range(half), range(half, half * 2)],
            [range(half, half * 2), range(half)],
            [range(half, half * 2), range(half, half * 2)]
        ]

        string += "("

        for xRange, yRange in chunkMap:
            dividedField = []
            for x in xRange:
                row = []
                for y in yRange:
                    row.append(field[x][y])
                dividedField.append(row)
            recursive(dividedField)
            
        string += ")"

recursive(field)
print(string)
