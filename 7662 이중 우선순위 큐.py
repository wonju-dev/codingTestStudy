from collections import deque


loop = int(input())

INF = int(1e9)
SIZE = 100000
HEAP = [INF] * SIZE
lastIndex = 0

def getLeftChildIndex(index):
    return index * 2 + 1

def getRightChildIndex(index):
    return index * 2 + 2

def getParentIndex(index):
    return (index - 1) // 2 if index % 2 == 1 else index // 2 - 1

def swapBottomUp(index):
    parentIndex = getParentIndex(index)
    if parentIndex < 0:
        return

    if HEAP[index] < HEAP[parentIndex]:
        HEAP[index], HEAP[parentIndex] = HEAP[parentIndex], HEAP[index]
        swapBottomUp(parentIndex)

def insert(number):
    global lastIndex
    if lastIndex >= SIZE:
        return

    HEAP[lastIndex] = number
    swapBottomUp(lastIndex)
    lastIndex += 1

def getBiggestIndex():
    global lastIndex
    
    size = lastIndex
    biggest = 0

    for i in range(size // 2, size, 1):
        leftChildIndex = getLeftChildIndex(i)
        rightChildIndex = getRightChildIndex(i)
        
        if leftChildIndex >= SIZE:
            break

        if HEAP[leftChildIndex] == INF and HEAP[rightChildIndex] == INF and HEAP[i] != INF:
            if HEAP[i] > HEAP[biggest]:
                biggest = i
    
    return biggest

def deleteBiggest():
    global lastIndex

    biggestIndex = getBiggestIndex()
    HEAP[biggestIndex] = INF
    lastIndex -= 1

def swapTopDown(index):
    leftChildIndex = getLeftChildIndex(index)
    rightChildIndex = getRightChildIndex(index)
    if leftChildIndex >= SIZE:
        return

    if HEAP[index] < HEAP[leftChildIndex] and HEAP[index] < HEAP[rightChildIndex]:
        return
    elif HEAP[index] > HEAP[leftChildIndex] and HEAP[index] < HEAP[rightChildIndex]:
        HEAP[index], HEAP[leftChildIndex] = HEAP[leftChildIndex], HEAP[index]
        swapTopDown(leftChildIndex)
    elif HEAP[index] < HEAP[leftChildIndex] and HEAP[index] > HEAP[rightChildIndex]:
        HEAP[index], HEAP[rightChildIndex] = HEAP[rightChildIndex], HEAP[index]
        swapTopDown(rightChildIndex)
    else:
        if HEAP[leftChildIndex] < HEAP[rightChildIndex]:
            HEAP[index], HEAP[leftChildIndex] = HEAP[leftChildIndex], HEAP[index]
            swapTopDown(leftChildIndex)
        else:
            HEAP[index], HEAP[rightChildIndex] = HEAP[rightChildIndex], HEAP[index]
            swapTopDown(rightChildIndex)


def deleteSmallest():
    if lastIndex == 0:
        return

    HEAP[0] = HEAP[lastIndex - 1]
    HEAP[lastIndex - 1] = INF
    swapTopDown(0)


for _ in range(loop):
    lastIndex = 0
    case = int(input())
    
    for g in range(case):
        op, number = input().split()
        number = int(number)

        if op == "I":
            insert(number)
        elif op == "D":
            if number == 1:
                deleteBiggest()
            elif number == -1:
                deleteSmallest()

    if HEAP[0] == INF:
        print("EMPTY")
    else:
        print(HEAP[getBiggestIndex()], HEAP[0])
        