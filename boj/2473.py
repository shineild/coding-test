import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

result = 10000000000

index = []
for i in range(n-2):
    l = i+1
    h = n-1
    while(l < h):
        tmp = arr[i] + arr[l] + arr[h]
        if abs(result) > abs(tmp):
            result = tmp
            index = [arr[i], arr[l], arr[h]]
        if tmp > 0:
            h -= 1
        elif tmp < 0:
            l += 1
        else:
            break
print(index[0], index[1], index[2])
