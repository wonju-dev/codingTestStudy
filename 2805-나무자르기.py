def cut(height: int) -> int:
    if height >= currentHeight:
        return height - currentHeight
    else:
        return 0


n, m = list(map(int, input().split()))
heights = list(map(int, input().split()))

highest = max(heights)

currentHeight = highest

while currentHeight > 0:
    cutSum = sum(list(map(cut, heights)))
    if cutSum >= m:
        print(currentHeight)
        break
    currentHeight -= 1
