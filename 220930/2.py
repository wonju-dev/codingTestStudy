# O(N^2)을 어떻게 개선?
# O(n)
case = int(input())

def findMax(values):
    index = 0
    for i in range(len(values)):
        if values[index] < values[i]:
            index = i
    return index

while case > 0:
    num = int(input())
    values = list(map(int,input().split()))
    ans = 0

    while len(values) > 1:
        maxIndex = findMax(values)
        # print(values, maxIndex)

        if maxIndex != 0:
            for i in range(maxIndex):
                ans += values[maxIndex] - values[i]
                # print(values[i], i, ans)

        values = values[maxIndex+1:]
    print(ans)

    case -=1

"""
3 3 7 9 7 4

5 5 10 1 1 9

2 5 10

9 5 4

10 9 8 7 6

11 5 5 10 1 1 9

9 8 7 1 2

1 2 3 1 1
"""