import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if (stack):
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if (stack):
            print(0)
        else:
            print(1)

    elif command[0] == "top":
        top = len(stack)-1
        if top == -1:
            print(-1)
        else:
            print(stack[top])
