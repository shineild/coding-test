import sys
n = int(input())
x= (sys.stdin.readlines(n))
x[0].rstrip()
y = []
y = x[0].split()
m = 0
for a in range(0, n):
    cnt = 0
    for b in range(0, n):
        if int(y[a]) < int(y[b]):
            cnt += 1
    if cnt == 0:
        m = int(y[a])
for a in range(0, n):
    y[a] = int(y[a])/m * 100
total = 0
for a in range(0, n):
    total += y[a]
avg = total/n
print(avg)
