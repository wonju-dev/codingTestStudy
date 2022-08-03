def solution(topping):
    frontIndex = 0
    backIndex = 0
    for i in range(len(topping)):
        front = topping[:i]
        back = topping[i:]
        if len(set(front)) == len(set(back)):
            frontIndex = i
            break

    for i in range(len(topping), -1, -1):
            front = topping[:i]
            back = topping[i:]
            if len(set(front)) == len(set(back)):
                backIndex = i
                break

    if backIndex == 0 and frontIndex == 0:
        return 0
    else:
        return backIndex - frontIndex + 1