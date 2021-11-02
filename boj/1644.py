import sys

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

n = int(sys.stdin.readline())
answer = 0
arr = prime_list(n+1)
l = len(arr)
for i in range(len(arr)):
    if i < l-1 and arr[i] + arr[i+1] > n:
        break
    p = i+2
    while(p <= l):
        if sum(arr[i:p]) == n:
            answer += 1
            break
        elif sum(arr[i:p]) < n:
            p += 1
        else:
            break

if l != 0 and arr[-1] == n:
    answer += 1

print(answer)
