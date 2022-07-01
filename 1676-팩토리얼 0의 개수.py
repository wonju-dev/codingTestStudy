def getFactorial(n: int) -> int:
    ans = 1
    for i in range(n, 0, -1):
        ans *= i
    return ans


def countZero(n: str) -> int:
    count = 0
    for i in range(len(n) - 1, 0, -1):
        if n[i] == "0":
            count += 1
        else:
            break
    return count


print(countZero(str(getFactorial(int(input())))))
