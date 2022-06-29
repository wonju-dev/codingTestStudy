def isMoreThanNeeds(mid: int) -> bool:
    heightSum = 0
    for tree in trees:
        if tree >= mid:
            heightSum += tree - mid
    return heightSum >= m


n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    if isMoreThanNeeds(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)
