k, n = map(int, input().split())
numbers = []

for i in range(k):
    numbers.append(int(input()))

start = 1
end = max(numbers)
ans = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for e in numbers:
        total += e // mid

    if total >= n:
        start = mid + 1
        if ans < mid:
            ans = mid
    elif total < n:
        end = mid - 1

print(ans)
