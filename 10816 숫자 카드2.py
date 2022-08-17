numbers = [0] * 20_000_001

n = int(input())
for number in list(map(int, input().split())):
    numbers[number] += 1

m = int(input())
for number in list(map(int, input().split())):
    print(numbers[number], end= " ")

