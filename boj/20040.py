import sys
n, m = map(int, sys.stdin.readline().split())
parent = [-1 for _ in range(n + 1)]

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

graph = []
finish = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if finish != 0:
        continue
    ar = find(a)
    br = find(b)
    if ar != br:
        union(ar, br)
    else:
        finish = i+1

print(finish)
