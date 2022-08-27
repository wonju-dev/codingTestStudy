case = int(input())

values = [25, 10, 5, 1]

for _ in range(case):
    change = int(input())  
    coins = [0, 0, 0, 0]
    index = 0
    while change > 0:
        share = change // values[index]
        change = change % values[index]

        coins[index] = share
        index += 1

    for i in range(4):
        if i != 3:
            print(coins[i], end=" ")
        else:
            print(coins[i])

