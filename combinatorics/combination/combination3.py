myNumbers = [1,2,3,4]

def getCombination(numbers, n):
    result = []

    if n == 0 :
        return [[]]

    for i in range(0, len(numbers)):
        elem = numbers[i]
        restNumbers = numbers[i + 1:]
        for c in getCombination(restNumbers, n - 1):
            result.append([elem] + c)

    return result

getCombination(myNumbers, 2)
getCombination(myNumbers, 3)
