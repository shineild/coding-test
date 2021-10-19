import sys
import heapq

n = int(sys.stdin.readline())
arr = []

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
i = 0
que = []
heapq.heappush(que, arr[0][1])

for i in range(1, n):
    if que[0] > arr[i][0]:
        heapq.heappush(que, arr[i][1])
    else:
        heapq.heappop(que)
        heapq.heappush(que, arr[i][1])
print(len(que))
