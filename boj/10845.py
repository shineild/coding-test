import sys

n = int(sys.stdin.readline())
que = []
for i in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "push":
        que.append(command[1])
    elif command[0] == "pop":
        if (que):
            print(que.pop(0))
        else:
            print(-1)
    elif command[0] == "size":
        print(len(que))
    elif command[0] == "empty":
        if (que):
            print(0)
        else:
            print(1)

    elif command[0] == "back":
        top = len(que)-1
        if top == -1:
            print(-1)
        else:
            print(que[top])
    elif command[0] == "front":
        if (que):
            print(que[0])
        else:
            print(-1)
