n = int(input())

counts = [0] * 2_000_001

for _ in range(n):
    counts[int(input()) + 1_000_000] += 1

for i in range(len(counts)):
    if counts[i] != 0:
        print(i - 1_000_000)