class Element:
    def __init__(self, num):
        self.num = num


def allocateId(num: str) -> Element:
    return Element(num)


def findMax(numbers):
    maxOne = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i].num > maxOne.num:
            maxOne = numbers[i]
    return maxOne


for _ in range(int(input())):
    n, m = map(int, input().split())
    numbers = list(map(allocateId, input().split()))

    targetNumber = numbers[m]
    justRemoved = 0
    counter = 0

    while len(numbers) != 0:
        first = numbers[0]
        maxOne = findMax(numbers)
        if first.num == maxOne.num and first is maxOne:
            justRemoved = first
            numbers = numbers[1:]
            counter += 1
            if justRemoved is targetNumber:
                print(counter)
                break
        else:
            numbers.append(first)
            numbers = numbers[1:]
