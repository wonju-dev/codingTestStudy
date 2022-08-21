from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2) // 2


    initQ1 = list(queue1)
    initQ2 = list(queue2)

    if sum1 == target and sum2 == target:
        return 0

    q = deque()
    q.append((queue1, queue2, 0))

    while q:
        q1, q2, count = q.popleft()

        if sum(q1) == target and sum(q2) == target:
            return count

        if initQ1 == q1 and initQ2 == q2 and count != 0:
            return -1
        else:
            # q1 pop, q2 insert
            if len(q1) >= 1:
                firstOne = q1[0]
                copyQ2 = list(q2)
                copyQ2.append(firstOne)
                q.append((q1[1:], copyQ2, count + 1))
            # q2 pop, q1 insert
            if len(q2) >= 1:
                firstOne = q2[0]
                copyQ1 = list(q1)
                copyQ1.append(firstOne)
                q.append((copyQ1, q2[1:], count + 1))

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1,1], [1,5]))