import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-tmp, tmp))
