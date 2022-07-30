import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
SIZE = 50
heap = [INF] * SIZE
lastIndex = 0

def getLeftIndex(index):
    return (index + 1) * 2 - 1

def getRightIndex(index):
    return (index + 1) * 2


def swapBottomUp(index):
    if index != 0:
        parentIndex = (index // 2) - 1 if index % 2 == 0 else (index - 1) // 2
        if abs(heap[parentIndex]) > abs(heap[index]):
            heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
            swapBottomUp(parentIndex)

def swapTopDown(index):
    leftIndex = getLeftIndex(index)
    rightIndex = getRightIndex(index)

    if rightIndex < SIZE:
        smallerSiblingIndex = leftIndex if abs(heap[leftIndex]) < abs(heap[rightIndex]) else rightIndex
        if abs(heap[index]) > abs(heap[smallerSiblingIndex]):
            heap[index], heap[smallerSiblingIndex] = heap[smallerSiblingIndex], heap[index]
            swapTopDown(smallerSiblingIndex)

def pop():
    popped = heap[0]
    heap[0] = INF
    
    global lastIndex
    leftIndex = getLeftIndex(lastIndex)
    rightIndex = getRightIndex(lastIndex)

    if rightIndex < SIZE:
        smallerSiblingIndex = leftIndex if abs(heap[leftIndex]) < abs(heap[rightIndex]) else rightIndex
        heap[0], heap[smallerSiblingIndex] = heap[smallerSiblingIndex], heap[0]
        swapTopDown(0)
    print(heap)
    return popped

def add(num):
    global lastIndex
    leftIndex = getLeftIndex(lastIndex)
    rightIndex = getRightIndex(lastIndex)

    if rightIndex < SIZE:
        for index in (lastIndex, leftIndex, rightIndex):
            if heap[index] == INF:
                heap[index] = num
                swapBottomUp(index)
                print(heap)
                break
        else:
            lastIndex += 1
            add(num)

for _ in range(n):
    num = int(input())
    
    if num != 0:
        add(num)
    elif num == 0 and heap[0] == INF:
        print(0)
    else:
        print(pop())
