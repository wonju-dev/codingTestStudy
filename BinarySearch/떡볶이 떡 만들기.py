n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

head = 0
tail = numbers[-1]


while head < tail:
    mid = (head + tail) // 2
    summation = 0

    for num in numbers:
        summation += num - mid if num - mid > 0 else 0

    if summation > m:
        head = mid + 1
    elif summation < m :
        tail = mid - 1
    else:
        print(mid)
        break