n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for _ in range(m):
    start, end = list(map(int, input().split()))
    answer = 0
    for i in range(start - 1, end):
        answer += numbers[i]
    print(answer)