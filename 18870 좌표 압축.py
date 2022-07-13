n = int(input())
numbers = list(map(int, input().split()))
sortedNumbers = sorted(set(numbers))


def binarySearch(n):
    head = 0
    tail = len(sortedNumbers)
    mid = (head + tail) // 2

    while head <= tail:
        mid = (head + tail) // 2
        if sortedNumbers[mid] < n:
            head = mid + 1
        elif sortedNumbers[mid] > n:
            tail = mid - 1
        else:
            return mid


for n in numbers:
    print(binarySearch(n))
