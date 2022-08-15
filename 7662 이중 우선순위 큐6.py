import heapq
import sys
input = sys.stdin.readline


loop = int(input())
for _ in range(loop):

    case = int(input())

    maxHeap = []
    minHeap = []
    isInUsed = [False] * 1_000_000

    for k in range(case):
        op, value = input().split()
        value = int(value)

        if op == "I":
            heapq.heappush(maxHeap, (-1 * value, k))
            heapq.heappush(minHeap, (value, k))
            isInUsed[k] = True

        elif op == "D":
            if value == 1:
                while maxHeap and not isInUsed[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    _, key = heapq.heappop(maxHeap)
                    isInUsed[key] = False

            elif value == -1:
                while minHeap and not isInUsed[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    _, key = heapq.heappop(minHeap)
                    isInUsed[key] = False

    while maxHeap and not isInUsed[maxHeap[0][1]]:
        heapq.heappop(maxHeap)                    

    while minHeap and not isInUsed[minHeap[0][1]]:
        heapq.heappop(minHeap)
        
    if maxHeap and minHeap:
        print(-1 * heapq.heappop(maxHeap)[0], heapq.heappop(minHeap)[0])
    else:
        print("EMPTY")