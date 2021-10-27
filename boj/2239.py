import sys

board = [list(map(int, list(str(sys.stdin.readline().rstrip()))))
         for _ in range(9)]
arr = []
nop = [[], [], [], [], [], [], [], [], []]
for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            if i//3 == 0:
                if j//3 == 0:
                    nop[0].append(board[i][j])
                elif j//3 == 1:
                    nop[1].append(board[i][j])
                elif j//3 == 2:
                    nop[2].append(board[i][j])
            elif i//3 == 1:
                if j//3 == 0:
                    nop[3].append(board[i][j])
                elif j//3 == 1:
                    nop[4].append(board[i][j])
                elif j//3 == 2:
                    nop[5].append(board[i][j])
            elif i//3 == 2:
                if j//3 == 0:
                    nop[6].append(board[i][j])
                elif j//3 == 1:
                    nop[7].append(board[i][j])
                elif j//3 == 2:
                    nop[8].append(board[i][j])
        else:
            arr.append([i, j])


def box(x, y):
    if x//3 == 0:
        if y//3 == 0:
            return 0
        elif y//3 == 1:
            return 1
        elif y//3 == 2:
            return 2
    if x//3 == 1:
        if y//3 == 0:
            return 3
        elif y//3 == 1:
            return 4
        elif y//3 == 2:
            return 5
    if x//3 == 2:
        if y//3 == 0:
            return 6
        elif y//3 == 1:
            return 7
        elif y//3 == 2:
            return 8

def ppp():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end="")
        print("")


def dfs(i):
    if i == len(arr):
        ppp()
        sys.exit(0)
    x = arr[i][0]
    y = arr[i][1]
    b = box(x, y)
    for k in range(1, 10):
        if not k in board[x]:
            c = 0
            for n in range(9):
                if k == board[n][y]:
                    c = 1
                    break
            if c == 1:
                continue
            if not k in nop[b]:
                board[x][y] = k

                nop[b].append(k)
                dfs(i+1)
                board[x][y] = 0
                nop[b].remove(k)


dfs(0)
