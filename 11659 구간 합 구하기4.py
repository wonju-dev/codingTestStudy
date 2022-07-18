import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sum = 0
results = [0]
for num in numbers:
    sum += num
    results.append(sum)

for _ in range(m):
    start, end = map(int, input().split())
    print(results[end] - results[start - 1])
