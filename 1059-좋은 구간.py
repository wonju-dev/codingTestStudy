length = int(input())
numbers = list(map(int, input().split()))
numbers.append(0)
numbers.sort()
n = int(input())

for i in range(len(numbers)):
    if n in numbers:
        print(0)
        break
    elif numbers[i] <= n and n <= numbers[i + 1]:
        print((n - numbers[i]) * (numbers[i + 1] - n) - 1)
        break
