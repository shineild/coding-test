
import sys
n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip()
         for i in range(n)]

def new_board(x, y):
    new = [board[dy][x:x+8] for dy in range(y, y+8)]
    return new

def wb(b):
    w_cnt = 0
    b_cnt = 0
    for y in range(len(b)):
        for x in range(len(b[y])):
            if y % 2 == 0:
                if x % 2 == 0:
                    if b[y][x] == 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if b[y][x] == 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
            else:
                if x % 2 == 0:
                    if b[y][x] == 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1
                else:
                    if b[y][x] == 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
    if w_cnt < b_cnt:
        return 64-b_cnt
    elif w_cnt > b_cnt:
        return 64-w_cnt
    else:
        return 32
mini = 64
for y in range(n-7):
    for x in range(m-7):
        new = new_board(x, y)
        cnt = wb(new)
        if cnt < mini:
            mini = cnt
print(mini)
