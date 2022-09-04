n = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

index = 0
count = 0

while index < len(numbers):
    index += numbers[index]
    if index > len(numbers):
        pass
    else:
        count += 1

print(count)