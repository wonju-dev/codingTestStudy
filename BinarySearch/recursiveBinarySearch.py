numbers = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def getIndex(array, number, head, tail):
    if head > tail:
        return -1

    mid = (head + tail) // 2

    if array[mid] < number:
        return getIndex(array, number, mid + 1, tail)
    elif number < array[mid]:
        return getIndex(array, number, head, mid - 1)
    else:
        return mid

print(getIndex(numbers, 6, 0, len(numbers) - 1))