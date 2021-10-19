h, w = map(int, input().split())
n = int(input())
namu = []
for i in range(0, n):
    buf = input().split()
    namu.append(buf)
higth = []
for i in range(0, h):
    width = [0]
    width = width * w
    higth.append(width)
for i in range(0, n):
    l = namu[i][0]
    b = namu[i][1]
    x = namu[i][2]
    y = namu[i][3]
    b = int(b)
    l = int(l)
    x = int(x) - 1
    y = int(y) - 1

    while(l > 0):
        higth[x][y] = 1
        if b == 0:
            y += 1
        else:
            x += 1
        l = l - 1
for i in range(0, h):
    for k in range(0, w):
        print(higth[i][k], end= " ")
    print("")
