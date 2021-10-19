import sys
n = int(input())
for a in range(0, n):
    avg = 0; cnt = 0;
    x = list(map(int, input().split()))
    for na in range(1, x[0]+1):
            avg += x[na]
    avg /= x[0]
    for c in range(1, x[0]+1):
        if x[c] > avg:
            cnt += 1
    print("%.3f%%" % round(float(cnt) / x[0] * 100, 3))
