n = int(input())
numbers = sorted(list(map(int, input().split())))

for i in range(1, n):
    if i != numbers[i - 1]:
        print(i)
        break
else:
    print(n + 1)