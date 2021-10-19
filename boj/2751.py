import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)
arr.sort()
for i in range(n):
    print(arr[i])
    
