import sys
a, b = map(int, input().split())
x= (sys.stdin.readlines(a))
x[0].rstrip()
y = []
y = x[0].split()
for n in range(0, a):
    if int(y[n]) < b:
        print(y[n], end = " ")
