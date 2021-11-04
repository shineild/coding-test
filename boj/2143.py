import sys
from collections import defaultdict
from typing import DefaultDict

dic_a = DefaultDict(int)

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(n):
    for j in range(i, n):
        dic_a[sum(a[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        ans += dic_a[t-sum(b[i:j+1])]

print(ans)
