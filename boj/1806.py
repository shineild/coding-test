import sys

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr_sum = [0] * (n + 1)

for i in range(1, n+1):
    arr_sum[i] = arr_sum[i-1] + arr[i-1]

short = n+1
start = 0
end = 1

while start != n:
    if arr_sum[end] - arr_sum[start] >= s:
        if end - start < short:
            short = end - start
        start += 1

    else:
        if end != n:
            end += 1
        else:
            start += 1
if short == n+1:
    print(0)
else:
    print(short)
