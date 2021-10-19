import sys
from collections import deque

def bfs(arr):
    q = deque('')
    q.append(0)
    dp[0] = 0
    while q:
        now = q.pop()
        jump = arr[now]
        for i in range(jump, 0, -1):
            if now + i < n and dp[now + i] == -1:
                dp[now + i] = dp[now] + 1
                q.appendleft(now + i)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [-1] * n
bfs(arr)
print(dp[-1])
