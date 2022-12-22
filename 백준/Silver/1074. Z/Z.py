n, r, c = list(map(int, input().split()))

field = [
    [(0, 0), (2 ** n // 2 - 1, 2 ** n // 2 - 1)],
    [(0, 2 ** n // 2), (2 ** n // 2 - 1, 2 ** n - 1)],
    [(2 ** n // 2, 0), (2 ** n - 1, 2 ** n // 2 - 1)],
    [(2 ** n // 2, 2 ** n // 2), (2 ** n - 1, 2 ** n - 1)],
]
count = 0


def findIndex(field):
    for i in range(len(field)):
        if field[i][0][0] == r and field[i][0][1] == c:
            return i


def getNewField(row):
    fx = row[0][0]
    fy = row[0][1]
    lx = row[1][0]
    ly = row[1][1]

    if lx - fx == 1 and ly - fy == 1:
        return [
            [(fx, fy), (fx, fy)],
            [(fx, fy + 1), (fx, fy + 1)],
            [(fx + 1, fy), (fx + 1, fy)],
            [(fx + 1, fy + 1), (fx + 1, fy + 1)],
        ]

    xRange = list(range(fx, lx + 1))
    yRange = list(range(fy, ly + 1))


    return [
        [
            (xRange[0], yRange[0]),
            (xRange[len(xRange) // 2 - 1], yRange[len(yRange) // 2 - 1]),
        ],
        [
            (xRange[0], yRange[len(yRange) // 2]),
            (xRange[len(xRange) // 2 - 1], yRange[-1]),
        ],
        [
            (xRange[len(xRange) // 2], yRange[0]),
            (xRange[-1], yRange[len(yRange) // 2 - 1]),
        ],
        [
            (xRange[len(xRange) // 2], yRange[len(yRange) // 2]),
            (xRange[-1], yRange[-1]),
        ],
    ]


def isInSection(section):
    first = section[0]
    end = section[1]

    return (first[0] <= r and r <= end[0]) and (first[1] <= c and c <= end[1])


def recursive(field, count):
    for i in range(4):
        if field[i][0][0] == field[i][1][0] and field[i][0][1] == field[i][1][1]:
            return count + findIndex(field)
        if isInSection(field[i]):
            return recursive(getNewField(field[i]), count)
        else:
            count += (field[i][1][0] - field[i][0][0] + 1) ** 2


print(recursive(field, count))
