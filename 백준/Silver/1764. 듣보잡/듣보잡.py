n, m = map(int, input().split())

unHeard = []
unSean = []

for _ in range(n):
    unHeard.append(input())

for _ in range(m):
    unSean.append(input())

unHeard = set(unHeard)
unSean = set(unSean)

unHeard = unHeard.intersection(unSean)
print(len(unHeard))
for e in sorted(list(unHeard)):
    print(e)
