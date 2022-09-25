from itertools import permutations

def solution(k, dungeons):

    cases = list(permutations(dungeons, len(dungeons)))

    result = 0

    for case in cases:
        hp = k
        count = 0
        for d in case:
            if hp >= d[0]:
                hp -= d[1]
                count += 1
            else:
                break
        if count > result:
            result = count

    return result