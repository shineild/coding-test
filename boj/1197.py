import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(v + 1)]
graph = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(graph, [c, a, b])

def find(x):
    if parent[x] < 0:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(x, y):
    if parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

cnt = v-1
answer = 0

while(cnt):
    d, a, b = heapq.heappop(graph)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        answer += d
        cnt -= 1
print(answer)
