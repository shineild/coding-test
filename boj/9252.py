import sys
a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

dp = [['' for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if a[j] == b[i]:
            dp[i+1][j+1] = dp[i][j] + a[j]
        else:
            if len(dp[i][j+1]) > len(dp[i+1][j]):
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]

print(len(dp[-1][-1]))
if len(dp[-1][-1]) != 0:
    print(dp[-1][-1])

