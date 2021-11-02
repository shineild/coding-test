import sys
from collections import deque


T = int(sys.stdin.readline())


def solve():
    n, k = map(int, sys.stdin.readline().split())
    delay = [0] + list(map(int, sys.stdin.readline().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    point = int(sys.stdin.readline())
    dp = [0 for _ in range(n+1)]
    q = deque()


    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = delay[i]

    while q:
        now = q.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now]+delay[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[point])


for _ in range(T):
    solve()
