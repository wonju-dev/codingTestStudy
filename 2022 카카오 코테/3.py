from itertools import product


def solution(users, emoticons):

    answer = [-1, -1]

    for discount in product([10, 20, 30, 40], repeat=len(emoticons)):
        discountedPrices = []
        for i in range(len(emoticons)):
            discountedPrices.append((discount[i] , emoticons[i] * (100 - discount[i]) / 100))
        
        member = 0
        benefit = 0
        for user in users:
            buyList = []
            cost = 0
            # print(discountedPrices)
            for i in range(len(discountedPrices)):
                percent, price = discountedPrices[i]
                # print(percent, price)
                if user[0] <= percent:
                    buyList.append(i)
                    cost += price
            if cost >= user[1]:
                member += 1
            else:
                benefit += cost

        if member > answer[0]:
            answer[0] = member
            answer[1] = benefit
        elif member == answer[0] and benefit > answer[1]:
            answer[1] = benefit

    return answer

# solution([[40, 10000], [25, 10000]], [7000, 9000])
# solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
