import sys

n, score, p = map(int, sys.stdin.readline().split())
if n == 0:
    print(1)
    exit()
arr = list(map(int, sys.stdin.readline().split()))
if min(arr) >= score:
    if n == p:
        print(-1)
    elif min(arr) == score:
        print(arr.index(min(arr))+1)
    else:
        print(n+1)
else:
    try:
        print(arr.index(score)+1)
    except:
        for i in range(len(arr)):
            if arr[i] < score:
                cnt = arr.count(arr[i])
                print(i+1)
                break
