numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def getIndex(array, number):

    head = 0
    tail = len(array) - 1

    while head <= tail:
        mid = (head + tail) // 2
        if array[mid] < number:
            head = mid + 1
        elif number < array[tail]:
            tail = mid - 1
        else:
            return mid
            
    return -1

print(getIndex(numbers, 3))