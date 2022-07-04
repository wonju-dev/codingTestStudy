n = int(input())

for i in range(1, n + 1):
    row = " " * (n - i) + "*" * i
    print(f"{row:}")
