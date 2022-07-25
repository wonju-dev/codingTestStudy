import heapq
import sys

heap = []

l = int(sys.stdin.readline())

for _ in range(l):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(heap) == 0:
            print(0);
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)