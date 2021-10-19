import sys
import bisect
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
mini = 2000000000
answer = []
while(True):
    target = -arr[0]
    t = bisect.bisect_left(arr, target)
    if t == len(arr):
        t -= 1
    elif t == 0:
        t = 1
    if t > 1:
        if abs(arr[t] + arr[0]) > abs(arr[t-1] + arr[0]):
            t -= 1
    tmp = arr[0] + arr[t]
    if tmp == 0:
        print(arr[0], arr[t])
        break
    if abs(mini) > abs(tmp):
        mini = arr[0] + arr[t]
        answer = [arr[0], arr[t]]
    del arr[0]
    if len(arr) == 1:
        print(answer[0], answer[1])
        break
