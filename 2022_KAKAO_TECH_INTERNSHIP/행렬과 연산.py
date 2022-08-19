from collections import deque


def solution(rc, operations):
    rc = deque(rc)

    for operation in operations:
        if operation == "Rotate":
            last = len(rc) - 1
            # first row
            firstRow = deque(rc[0])
            firstRow.appendleft(rc[1][0])
            firstRowLast = firstRow.pop()
            rc[0] = list(firstRow)
            ## print(f"firstRow={rc[0]}")

            # last row
            lastRow = deque(rc[last])
            lastRow.append(rc[last - 1][-1])
            lastRowFirst = lastRow.popleft()
            rc[last] = list(lastRow)
            ## print(f"lastRow={rc[last]}")
            # right
            for i in range(last - 1, 1, -1):
                rc[i][-1] = rc[i-1][-1]
            rc[1][-1] = firstRowLast
            ## print(f"rc[1][-1]={rc[1][-1]}")
            # left
            for i in range(1, last - 1):
                rc[i][0] = rc[i+1][0]
            rc[last - 1][0] = lastRowFirst
            ## print(f"rc[last - 1][-1]={rc[last - 1][-1]}")
            # update
        elif operation == "ShiftRow":
            rc.appendleft(rc.pop())

    return list(rc)

print(solution([[1,2,3],[4,5,6],[7,8,9]], ["Rotate", "ShiftRow"]))
print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
