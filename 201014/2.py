testCase = int(input())

def bi(num):

    index = 0

    while True:
        if num < 2 ** index:
            return 2 ** index
        index += 1

while testCase > 0 :
    case = int(input())

    arrays = {
        # [현재 원소 개수, 배열 크기]
    }
    count = 0

    while case > 0 :
        a, c = map(int, input().split())

        if a in arrays:
            if arrays[a][0] + c > arrays[a][1]:
                count += arrays[a][0]
                arrays[a][1] = bi(arrays[a][0] + c)
            arrays[a][0] += c
        else:
            arrays[a] = [c, bi(c)]

        # print(arrays)

        case -= 1
    print(count)

    testCase -= 1