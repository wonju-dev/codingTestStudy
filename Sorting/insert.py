import random
import time

def insertSort(numbers):
    pivot = 1
    while pivot < len(numbers):
        for i in range(pivot):
            if numbers[i] >= numbers[pivot]:
                numbers.insert(i, numbers[pivot])
                numbers = numbers[0:pivot + 1] + numbers[pivot + 2 :]
                break
        pivot += 1
    return numbers


def insertSort2(numbers):
    for i in range(1, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            else:
                break
    return numbers

numbers = []
for i in range(50000):
    rn = random.randint(1, 50000)
    numbers.append(rn)
numbers2 = list(numbers)

st = time.time()
insertSort(numbers)
print(time.time() - st)

st = time.time()
insertSort2(numbers2)
print(time.time() - st)
