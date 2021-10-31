import sys
import heapq
n = int(sys.stdin.readline())
parent = {}
graph = []

def find(x):
    if parent[x] == False:
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


for _ in range(n):
    x, y = map(float, sys.stdin.readline().split())
    parent[(x, y)] = False
    graph.append((x, y))

arr = []

for i in range(n-1):
    a = graph[i][0]
    b = graph[i][1]
    for j in range(i+1, n):
        x = graph[j][0]
        y = graph[j][1]
        dx = abs(a-x)
        dy = abs(b-y)
        l = round((dx**2 + dy**2)**0.5, 2)
        heapq.heappush(arr, [l, (a, b), (x, y)])

cnt = n-1
answer = 0

while(cnt):
    l, a, b = heapq.heappop(arr)
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
        answer += l
        cnt -= 1
print(answer)
