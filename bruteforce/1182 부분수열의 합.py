from itertools import combinations

n, s = map(int, input().split())

numbers = list(map(int, input().split()))

count = 0
for i in range(1, n + 1):
    combis = combinations(numbers, i)
    for pair in combis:
        if sum(list(pair)) == s:
            count += 1
print(count)