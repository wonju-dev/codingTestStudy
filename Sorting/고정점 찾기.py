n = int(input())
numbers = list(map(int, input().split()))

head = 0
tail = n - 1
while head <= tail:
    mid = (head + tail) // 2

    if mid > numbers[mid]:
        head = mid + 1
    elif mid < numbers[mid]:
        tail = mid - 1
    else:
        print(mid)
        break
else:
    print(-1)