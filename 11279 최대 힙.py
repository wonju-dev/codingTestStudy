n = int(input())
heap = [-1] * 100000
lastIndex = 0

def getLeftIndex(index):
    return (index + 1) * 2 - 1

def getRightIndex(index):
    return (index + 1) * 2

def swapBottomUp(index):
    if index != 0:
        parentIndex = (index // 2) - 1 if index % 2 == 0 else (index - 1) // 2
        if heap[parentIndex] < heap[index]:
            heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
            swapBottomUp(parentIndex)

def swapTopDown(index):
    leftIndex = getLeftIndex(index)
    rightIndex = getRightIndex(index)

    biggerSiblingIndex = leftIndex if heap[leftIndex] > heap[rightIndex] else rightIndex
    if heap[index] < heap[biggerSiblingIndex]:
        heap[index], heap[biggerSiblingIndex] = heap[biggerSiblingIndex], heap[index]
        swapTopDown(biggerSiblingIndex)
        return

def add(num):
    global lastIndex

    for index in (lastIndex, getLeftIndex(lastIndex), getRightIndex(lastIndex)):
        if heap[index] == -1:
            heap[index] = num
            swapBottomUp(index)
            return
    else:
        lastIndex += 1
        add(num)

def pop():
    popped = heap[0]
    heap[0] = -1
    
    global lastIndex
    leftIndex = getLeftIndex(lastIndex)
    rightIndex = getRightIndex(lastIndex)

    biggerSiblingIndex = leftIndex if heap[leftIndex] > heap[rightIndex] else rightIndex
    heap[0], heap[biggerSiblingIndex] = heap[biggerSiblingIndex], heap[0]
    swapTopDown(0)
        
    return popped

for _ in range(n):
    num = int(input())
    
    if num != 0:
        add(num)
    elif num == 0 and heap[0] == -1:
        print(0)
    else:
        print(pop())
