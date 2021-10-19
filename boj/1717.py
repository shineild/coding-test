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
for _ in range(m):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0:
        ar = find(a)
        br = find(b)
        if ar != br:
            union(ar, br)
    if x == 1:
        ar = find(a)
        br = find(b)
        if ar == br:
            print("YES")
        else:
            print("NO")
