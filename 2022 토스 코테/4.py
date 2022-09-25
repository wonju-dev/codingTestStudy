from collections import deque

def solution(invitationPairs):
    invitationMap = {}
    lastMember = 0

    for pair in invitationPairs:
        invitor, guest = pair
        if invitor > lastMember:
            lastMember = invitor
        if guest > lastMember:
            lastMember = guest

        if invitationMap.get(invitor) is not None:
            invitationMap[invitor].append(guest)
        else:
            invitationMap[invitor] = [guest]

    graph = [[] for _ in range(lastMember + 1)]

    for key, value in invitationMap.items():
        graph[key] = value

    scores = []


    for key, value in invitationMap.items():
        q = deque()

        for member in value:
            q.append((member, 1))
        
        score = 0

        while q:
            member, relationship = q.pop()
            if relationship == 1:
                score += 10
            elif relationship == 2:
                score += 3
            else:
                score += 1
            
            if invitationMap.get(member) is not None:
                for childMember in invitationMap[member]:
                    q.append((childMember, relationship + 1))

        scores.append((key, score))

    scores.sort(key= lambda x: x[1], reverse=True)
    answer = []
    if len(scores) >= 3:
        answer = [scores[0][0], scores[1][0], scores[2][0]]
    else:
        for i in range(len(scores)):
            answer.append(scores[i][0])
    return answer
    