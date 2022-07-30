n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
m = int(input())
target = list(map(int, input().split()))

for t in target:
    head = 0
    tail = len(numbers) - 1

    while head <= tail:
        mid = (head + tail) // 2
        
        if numbers[mid] < t:
            head = mid + 1
        elif t < numbers[mid]:
            tail = mid - 1
        elif numbers[mid] == t:
            print("yes", end=" ")
            break
    else:
        print("no", end=" ")