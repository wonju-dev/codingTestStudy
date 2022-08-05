import sys
input = sys.stdin.readline

SIZE = 100000
INF = int(1e9)
lastIndex = 0

n = int(input())
heap = [INF] * SIZE

def swapTopDown(index):
    leftChildIndex = index * 2 + 1
    rightChildIndex = index * 2 + 2
    if leftChildIndex > SIZE and rightChildIndex > SIZE:
        return
    
    if abs(heap[leftChildIndex]) > abs(heap[rightChildIndex]):
        smallerChildIndex = rightChildIndex
    elif abs(heap[leftChildIndex]) < abs(heap[rightChildIndex]):
        smallerChildIndex = leftChildIndex
    else:
        if heap[leftChildIndex] <= heap[rightChildIndex]:
            smallerChildIndex = leftChildIndex
        else:
            smallerChildIndex = rightChildIndex
            
    # print(f"smallerChildIndex: {smallerChildIndex}")

    if heap[smallerChildIndex] != INF:
        if abs(heap[index]) > abs(heap[smallerChildIndex]):
            heap[index], heap[smallerChildIndex] = heap[smallerChildIndex], heap[index]
            swapTopDown(smallerChildIndex)
        elif abs(heap[index]) == abs(heap[smallerChildIndex]) and heap[index] > heap[smallerChildIndex]:
            heap[index], heap[smallerChildIndex] = heap[smallerChildIndex], heap[index]
            swapTopDown(smallerChildIndex)

def pop():

    global lastIndex

    minimum = heap[0]
    heap[0] = heap[lastIndex - 1]
    heap[lastIndex - 1] = INF
    # print(f"heap: {heap}")
    swapTopDown(0)

    if lastIndex - 1 < 0:
        lastIndex = 0
    else:
        lastIndex -= 1

    return minimum

def getParentIndex(index):
    return index // 2 - 1 if index % 2 == 0 else (index - 1) // 2

def swapBottomUp(index):
    if index == 0:
        return

    parentIndex = getParentIndex(index)

    if parentIndex < SIZE and index < SIZE:
        if abs(heap[parentIndex]) > abs(heap[index]):
            heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
            swapBottomUp(parentIndex)
        elif heap[parentIndex] * -1 == heap[index] and heap[parentIndex] > heap[index]:
            heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
            swapBottomUp(parentIndex)

def insert(number):
    global lastIndex

    if heap[lastIndex] == INF and lastIndex < SIZE:
        heap[lastIndex] = number
        swapBottomUp(lastIndex)
        lastIndex += 1

def start(n):
    for _ in range(n):
        number = int(input())
        
        if number == 0:
            if heap[0] != INF:
                print(pop())
            else:
                print(0)
        else:
            insert(number)

        # print(heap)

start(n)