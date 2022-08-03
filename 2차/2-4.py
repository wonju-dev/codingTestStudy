def findLowerBound(topping):
    head = 0
    tail = len(topping)
    mid = (head + tail) // 2

    while len(set(topping[:mid])) != len(set(topping[mid:])):
        if len(set(topping[:mid])) < len(set(topping[mid:])):
            head = mid + 1
        elif len(set(topping[:mid])) >= len(set(topping[mid:])):
            tail = mid - 1

        mid = (head + tail) // 2

    return mid

def findUpperBound(topping):
    head = 0
    tail = len(topping)
    mid = (head + tail) // 2

    while len(set(topping[:mid])) != len(set(topping[mid:])) or head <= tail:
        if len(set(topping[:mid])) <= len(set(topping[mid:])):
            head = mid + 1
        elif len(set(topping[:mid])) > len(set(topping[mid:])):
            tail = mid - 1

        mid = (head + tail) // 2

    return mid

def solution(topping):

    lowerBound = findLowerBound(topping)
    upperBound = findUpperBound(topping)

    return lowerBound - upperBound

print(solution([1,2,1,3,1,4,1,2]))
# print(solution([1,2,3,1,4]))
# print(solution([1,1,1,1,1]))