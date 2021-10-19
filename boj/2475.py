import sys

arr = list(map(int, sys.stdin.readline().split()))
hap = 0
for i in arr:
    hap += i * i
print(hap % 10)
