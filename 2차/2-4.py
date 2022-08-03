def findLowerBound(topping):
    head = 0
    tail = len(topping)
    mid = (head + tail) // 2

    while head != tail != mid:
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

    while head != tail != mid:
        if len(set(topping[:mid])) <= len(set(topping[mid:])):
            head = mid + 1
        elif len(set(topping[:mid])) > len(set(topping[mid:])):
            tail = mid - 1

        mid = (head + tail) // 2

    return mid

def solution(topping):

    lowerBound = findLowerBound(topping)
    upperBound = findUpperBound(topping)


    return upperBound - lowerBound
