import sys
import heapq
input = lambda : sys.stdin.readline().strip()
n, k = map(int, input().split())
arr = []
for i in range(n):
    m, v = map(int,input().split())
    heapq.heappush(arr, [m, v])
back = [int(input()) for _ in range(k)]
back.sort()
gold = 0
gem = []
for i in range(k):
    while (arr and back[i] >= arr[0][0]):
        x, p = heapq.heappop(arr)
        heapq.heappush(gem, -p)
    if gem:
        gold -= (heapq.heappop(gem))
    elif not arr:
        break

print(gold)
