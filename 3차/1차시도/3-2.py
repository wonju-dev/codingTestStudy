def solution(distance, scope, times):
    for i in range(len(times)):
        period = times[i][0] + times[i][1]
        for j in range((distance // period) + 1):
            for time in range(period * j + 1, period * j + times[i][0] + 1):
                if scope[i][0] <= time <= scope[i][1]:
                    return time
    
    return distance

# 실패 (35.7 / 100)