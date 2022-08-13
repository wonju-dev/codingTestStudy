def isWorking(now, work, rest, distance):
    period = work + rest
    for i in range((distance // period) + 1):
        workingRange = range(period * i + 1, period * i + work + 1)
        if now in workingRange:
            return True
    return False

def solution(distance, scopes, times):
    d = 0
    # 매 위치(초)에 대해
    for d in range(1, distance + 1):
        for s in range(len(scopes)):
            # s 초 일때 구간에 속함?
            if d in range(scopes[s][0], scopes[s][1] + 1):
                # s 초 일때 일하는 중?
                if isWorking(d, times[s][0], times[s][1], distance):
                    return d

    return d  

# 실패 (시간초과 + 실패) / 71.4 / 1000