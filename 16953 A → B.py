from collections import deque


n, m = map(int, input().split())

q = deque()
q.append([n, 0])

while q:
    number, count = q.popleft()

    if number == m:
        print(count + 1)
        break

    if number < m:
        q.append([number * 2, count + 1])
        q.append([int(str(number) + "1"), count + 1])
else:
    print(-1)
