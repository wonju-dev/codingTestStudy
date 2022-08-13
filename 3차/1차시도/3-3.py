def solution(distance, scope, times):
    for i in range(len(times)):
        # '일하는 시간 + 쉬는 시간' 주기로 반복
        period = times[i][0] + times[i][1]
        # 해당 시간에 일하는 범위 정렬
        start, end = scope[i]
        if start > end:
            start, end = end, start

        for j in range((distance // period) + 1):
            # 일하는 시간에 대해
            for time in range(period * j + 1, period * j + times[i][0] + 1):
                # 예외 처리
                if time > distance or time > end:
                    break
                # 일하는 시간에, 경비하는 위치에 있으면 발각
                if start <= time <= end:
                    return time
    
    return distance

# 실패 (42.9 / 100)