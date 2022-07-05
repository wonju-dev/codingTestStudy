n, r, c = list(map(int, input().split()))
field = []
count = 0

for a in range(2 ** n):
    row = []
    for b in range(2 ** n):
        row.append((a, b))
    field.append(row)


def getSection(field, index):
    section = []
    length = len(field)

    if index == 0:
        for a in range(length // 2):
            section.append(field[a][: length // 2])
    if index == 1:
        for a in range(length // 2):
            section.append(field[a][length // 2 : length])
    if index == 2:
        for a in range(length // 2, length):
            section.append(field[a][: length // 2])
    if index == 3:
        for a in range(length // 2, length):
            section.append(field[a][length // 2 : length])

    return section


def isInSection(section):
    first = section[0][0]
    end = section[len(section) - 1][len(section) - 1]

    return (first[0] <= r and r <= end[0]) and (first[1] <= c and c <= end[1])


def recursive(field, count):
    if len(field) == 1 and len(field[0]) == 1:
        return count

    for i in range(4):
        section = getSection(field, i)
        if isInSection(section):
            return recursive(section, count)
        else:
            count += len(section) ** 2


print(recursive(field, count))
