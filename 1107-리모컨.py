from itertools import product

target = int(input())
n = int(input())
brokens = list(map(str, input().split()))
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
availableNumbers = list(set(NUMBERS) - set(brokens))

if len(availableNumbers) == 0:
    print(abs(target - 100))
else:
    availables = list(product(availableNumbers, repeat=len(str(target)) + 1))

    closest = int("".join(availables[0]))
    for number in availables:
        newNumber = int("".join(number))
        if abs(target - closest) > abs(target - newNumber):
            closest = newNumber

    print(min([abs(100 - target), len(str(closest)) + abs(target - closest)]))