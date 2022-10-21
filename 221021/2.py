testCase = int(input())

while testCase > 0:

    n, a = map(int, input().split())

    picture = []

    rotatedPicture = [[] for _ in range(n)]

    for _ in range(n):
        picture.append(input())

    if a in [90, -270]:
        for y in range(n):
            col = []
            for x in range(n - 1 , -1, -1):
                col.append(picture[x][y])
            rotatedPicture[y] = col

    elif a in [-90, 270]:
        for y in range(n - 1, -1, -1):
            col = []
            for x in range(n):
                col.append(picture[x][y])
            rotatedPicture[n - y - 1] = col
    elif a in [180, -180]:
        for x in range(n - 1, -1, -1):
            row = []
            for y in range(n -1 , -1, -1):
                row.append(picture[x][y])
            rotatedPicture[n - x - 1] = row

    else:
        rotatedPicture = picture
    
    for x in range(n):
        for y in range(n):
            print(rotatedPicture[x][y], end="")
        print()

    testCase -= 1