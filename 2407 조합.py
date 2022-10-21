n, m = map(int, input().split())

ans = 1

for i in range(m):
    ans *= n
    n -= 1
sm = m
for i in range(sm):
    ans //= m
    m -= 1

print(int(ans))
