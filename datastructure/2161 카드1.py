from collections import deque


n = int(input())

q = deque(range(1, n + 1))

trace = ""
while len(q) != 1:
    top = q.popleft()
    trace += str(top) + " "
    
    nextTop = q.popleft()
    q.append(nextTop)

print(trace + str(q[0]))