road = []
for i in range(0, 10):
    buf = input().split()
    road.append(buf)
x = 0
y = 0
stop = 0
for i in range(0, 10):
    for k in range(0, 10):
        if road[i][k] == '0':
            x = i
            y = k
            stop = 1
        if stop == 1:
            break
while(x != 9 or y != 9):
    if road[x][y] == '2':
        road[x][y] = '9'
        break
    elif road[x][y] == '0':
        road[x][y] = '9'
    if road[x][y+1] != '1':
        y += 1
    elif road[x+1][y] != '1':
        x += 1
    else:
        break
for i in range(0, 10):
    for k in range(0, 10):
        print(road[i][k], end=" ")
    print("")
