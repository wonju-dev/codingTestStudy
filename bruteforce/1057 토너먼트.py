from collections import deque

# 데이터 초기화
n, a, b = map(int, input().split())
target = [a, b]
q = deque([i for i in range(1, n + 1)])

# 라운드 횟수
count = 1
# 종료 조건 
finish = False

# 최후의 1인이 남을때 까지 반복
while len(q) != 1:
    # 이번 라운드의 우승자들 보관
    winners = []

    # 차례대로 2명 뽑음
    for i in range(len(q) // 2):
        one = q.popleft()
        two = q.popleft()
        # 해당 2명이면 종료
        if one in target and two in target:
            print(count)
            finish = True
            break
        # 둘 중에 한 명이 포함되면 이긴걸로 만들기
        elif one in target:
            winners.append(one)
        elif two in target:
            winners.append(two)
        # 찾으려는 두 명이 아니면 아무나 올리기
        else:
            winners.append(one)
    
    # 만약 이번 라운드에 경기를 안 한 사람이 한 명 남았으면(홀수), 다음 라운드로 진출
    last = -1
    if len(q) == 1:
        last = q.popleft()

    if finish:
        break
    
    for winner in winners:
        q.append(winner)
    # 이번 라운드에 경기 안 한 사람은 마지막 순서로 다음 라운드 진출 시킴
    if last != -1:
        q.append(last)
    
    count += 1
        