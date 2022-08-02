l = int(input())

for _ in range(l):
    n, m, x, y = map(int, input().split())
    n -= 1; m -= 1; x -= 1; y -= 1
    nCounter = 0
    mCounter = 0

    index = 0

    while index < n * m:
        # print(nCounter, mCounter, index)
        if x == nCounter and y == mCounter:
            print(index + 1)
            break

        nCounter = (nCounter + 1) % (n + 1)
        mCounter = (mCounter + 1) % (m + 1)
        index += 1
    else:
        print(-1)