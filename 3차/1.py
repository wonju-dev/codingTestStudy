def solution(a, b, n):
    answer = 0

    while n // a >= 1:
        share = n // a
        remainder = n % a
        
        answer += share * b

        n = remainder + share * b

    return answer