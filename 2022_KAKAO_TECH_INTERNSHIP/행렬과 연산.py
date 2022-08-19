from collections import deque


def solution(rc, operations):
    rc = deque(rc)

    for operation in operations:
        if operation == "Rotate":
            last = len(rc) - 1
            firstRowLast = rc[0][-1]
            lastRowFirst = rc[last][0]

            # first row
            rc[0] = [rc[1][0]] + rc[0][:-1]
            
            # last row
            rc[last] = rc[last][1:] + [rc[last - 1][-1]]
            
            # right
            for i in range(len(rc) - 2, 1, -1):
                rc[i][-1] = rc[i - 1][-1]
            rc[1][-1] = firstRowLast
            # left
            for i in range(1, len(rc) - 2):
                rc[i][0] = rc[i + 1][0]
            rc[last - 1][0] = lastRowFirst
        elif operation == "ShiftRow":
            lastRow = rc.pop()
            rc.appendleft(lastRow)

    return list(rc)

# print(solution([[1,2,3],[4,5,6],[7,8,9]], ["Rotate", "ShiftRow"]))
# print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
# print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
