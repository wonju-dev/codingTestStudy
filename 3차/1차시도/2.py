def solution(ingredient):
    if len(ingredient) <= 3:
        return 0

    count = 0
    i = 0
    while i <= len(ingredient) - 4:
        # print(ingredient, i, ingredient[i], ingredient[i+1], ingredient[i+2], ingredient[i+3])
        if ingredient[i] == 1 and ingredient[i+1] == 2 and ingredient[i+2] == 3 and ingredient[i+3] == 1:
            count += 1
            ingredient = ingredient[:i] + ingredient[i+4:]
            i = 0
        else:
            i += 1
    else:
        return count
# 시간초과 (47.1 / 1000)