from collections import deque


s, t = map(int, input().split())

if s == t:
    print(0)
else:
    q = deque()
    q.append([s, ""])

    didOne = False

    while q:

        now, his = q.popleft()

        # print(f"now={now}, his={his}")
        
        if now == t:
            print(his)
            break
        else:
            multiply = (now * now, "*")
            plus = (now * 2, "+")
            divide = (1, "/")

            for value in [multiply, plus, divide]:
                if value[0] <= t:
                    if value[0] == 1:
                        if not didOne:
                            didOne = True
                            q.append((value[0], his + value[1]))
                    else:
                        q.append((value[0], his + value[1]))

    else:
        print(-1)


"""
7 * 7
    (7 * 7) ^ 2
        (7 * 7) ^ 2 ^ 2
        (7 * 7) ^ 2 * 2
        0
        1
    (7 * 7) * 2
        ((7 * 7) * 2) ^ 2
        (7 * 7) * 2 * 2
        0
        1
    0
    1
        1
        2
        0
        1

7 + 7
    (7 + 7) ^ 2
    (7 + 7) * 2
    0
    1

0
    0
    0
    0

1
    1
        1
        2
        0
        1
    2
        4
        4
        0
        1
    0
    1
        1
        2
        0
        1

"""