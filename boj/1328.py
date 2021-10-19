import sys
N, L, R = map(int, sys.stdin.readline().split())
dp = [[[0 for a in range(R + 1)] for b in range(L + 1)] for c in range(N + 1)]
dp[1][1][1] = 1
for n in range(2, N + 1):
    for l in range(1, L + 1):
        for r in range(1, R + 1):
            dp[n][l][r] = (dp[n-1][l][r]*(n-2)
                           + dp[n-1][l][r-1]
                           + dp[n-1][l-1][r])
            dp[n][l][r] %= 1000000007
print(dp[N][L][R])
