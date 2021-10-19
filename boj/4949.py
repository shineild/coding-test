import sys
from collections import deque
while(1):
    string = sys.stdin.readline()
    if string == '.\n':
        break
    que = deque('')
    result = ""
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            que.append(string[i])
        elif string[i] == ')':
            if not que:
                result = "no"
                break
            elif que[-1] == '(':
                que.pop()
            else:
                result = "no"
        elif string[i] == ']':
            if not que:
                result = "no"
            elif que[-1] == '[':
                que.pop()
            else:
                result = "no"
    if result:
        print(result)
    elif not que:
        print("yes")
    else:
        print("no")
