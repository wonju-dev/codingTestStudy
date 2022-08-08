def solution(topping):
    answer = 0
    for i in range(len(topping)):
        front = topping[:i]
        back = topping[i:]
        if len(set(front)) == len(set(back)):
            answer += 1

    return answer