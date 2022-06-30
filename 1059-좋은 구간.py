length = int(input())
numbers = list(map(int, input().split()))
n = int(input())
answer = 0

if n in numbers:
    print(0)
else:
    numbers.sort()

    head = 0
    tail = len(numbers) - 1

    while head <= tail:
        mid = (head + tail) // 2

        if n < numbers[mid]:
            tail = mid - 1
        elif n > numbers[mid]:
            head = mid + 1

    head, tail = tail, head

    if head == -1:
        for i in range(1, n + 1):
            for j in range(i + 1, numbers[tail]):
                answer += 1
        print(answer)
    else:
        start = numbers[head] + 1
        end = numbers[tail] - 1
        for i in range(start, n + 1):
            for j in range(i + 1, end + 1):
                answer += 1
        print(answer)
