import sys


n = int(sys.stdin.readline())
bfs = [[0, []] for _ in range(n + 1)]
bfs[1][0] = 0
bfs[1][1] = [1]
for i in range(2, n+1):
    bfs[i][0] = bfs[i-1][0] + 1
    bfs[i][1] = bfs[i-1][1] + [i]

    if i % 3 == 0 and bfs[i//3][0] + 1 < bfs[i][0]:
        bfs[i][0] = bfs[i//3][0] + 1
        bfs[i][1] = bfs[i//3][1] + [i]
    if i % 2 == 0 and bfs[i//2][0] + 1 < bfs[i][0]:
        bfs[i][0] = bfs[i//2][0] + 1
        bfs[i][1] = bfs[i//2][1] + [i]

print(bfs[n][0])

for i in bfs[n][1][::-1]:
    print(i, end=" ")
print("")
