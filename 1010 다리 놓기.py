case = int(input())

def recursive(n, m):
    if n == 1:
        return m
    else:
        summation = 1
        for i in range(1, m - n + 1):
            summation += recursive(n - 1, m - i)
        return summation

for _ in range(case):
    n, m = map(int, input().split())
    print(recursive(n, m))

