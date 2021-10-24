import sys
r, c = map(int, sys.stdin.readline().split())
alpha = [0] * 26
# in을 쓰기 보다는 인덱스로 확인할 수 있으면 인덱스로 확인하자
max_cnt = 0

board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(r)]
def dfs(x, y, cnt):
    alpha[board[x][y]] = 1

    global max_cnt
    max_cnt = max(max_cnt, cnt)
    bt = 0
    if x+1 < r:
        if alpha[board[x+1][y]] == 0:
            dfs(x+1, y, cnt+1)
    if x-1 >= 0:
        if alpha[board[x-1][y]] == 0:
            dfs(x-1, y, cnt+1)
    if y+1 < c:
        if alpha[board[x][y+1]] == 0:
            dfs(x, y+1, cnt+1)
    if y-1 >= 0:
        if alpha[board[x][y-1]] == 0:
            dfs(x, y-1, cnt+1)
    alpha[board[x][y]] = 0
    return


dfs(0, 0, 1)
print(max_cnt)
