def solution(topping):
    answer = 0
    m1 = {}
    m2 = {}

    for i in topping:
        if m1.get(i) is not None:
            m1[i] = m1[i] + 1
        else:
            m1[i] = 1
            
    for i in topping:
        m1[i] = m1[i] - 1
        if m1[i] == 0:
            del m1[i]
        
        if m2.get(i) is not None:
            m2[i] = m2[i] + 1
        else:
            m2[i] = 1

        if len(m1.values()) == len(m2.values()):
            answer += 1
        print(m1, m2)

    return answer

print(solution([1,2,1,3,1,4,1,2]))
print(solution([1,2,3,1,4]))