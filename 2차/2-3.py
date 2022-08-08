def solution(topping):
    answer = -1
    
    head = 0
    tail = len(topping)

    startIndex = 0

    while head <= tail:
        mid = (head + tail) // 2
        if len(set(topping[:mid])) > len(set(topping[:mid])):
            tail = mid - 1
        elif len(set(topping[:mid])) < len(set(topping[:mid])):
            head = mid + 1
        else:   
            startIndex = mid
            answer += 1
            break

    # 아래 방향
    goDown = startIndex

    while len(set(topping[:goDown])) == len(set(topping[goDown:])):
        answer += 1
        goDown -= 1
    # 윗 방향

    goUp = startIndex + 1
    while len(set(topping[:goUp])) == len(set(topping[goUp:])):
        answer += 1
        goUp += 1

    return answer
