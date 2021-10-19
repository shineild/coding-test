import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
best_gap = 300001
for a in range(n):
    for b in range(n):
        if b == a:
            continue

        for c in range(n):
            if c == b or c == a:
                continue
            result = arr[a] + arr[b] + arr[c]
            if result <= m:
                gap = m - result
                if gap < best_gap:
                    best_gap = gap
                    blackjack = result
print(blackjack)
