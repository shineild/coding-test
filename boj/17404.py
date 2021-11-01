import sys

n = int(sys.stdin.readline())

dp = [[0] * 3 for _ in range(n)]

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp[0][0] = arr[0][0]
dp[0][1] = 1001
dp[0][2] = 1001
for i in range(1, n-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + arr[i][2]

red = min(min(dp[n-2][0], dp[n-2][2]) + arr[n-1][1],
          min(dp[n-2][0], dp[n-2][1]) + arr[n-1][2])

dp[0][0] = 1001
dp[0][1] = arr[0][1]
dp[0][2] = 1001
for i in range(1, n-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + arr[i][2]

green = min(min(dp[n-2][1], dp[n-2][2]) + arr[n-1][0],
            min(dp[n-2][0], dp[n-2][1]) + arr[n-1][2])

dp[0][0] = 1001
dp[0][1] = 1001
dp[0][2] = arr[0][2]
for i in range(1, n-1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + arr[i][2]

blue = min(min(dp[n-2][1], dp[n-2][2]) + arr[n-1][0],
           min(dp[n-2][0], dp[n-2][2]) + arr[n-1][1])

print(min(red, green, blue))
