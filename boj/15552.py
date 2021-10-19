import sys
n = int(input())
for a in range(0, n):
    x= (sys.stdin.readlines(1))
    q, w = x[0].split()
    print(int(q) + int(w))
