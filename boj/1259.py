import sys
n = 1
while (True):
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    elif n == n[::-1]:
        print("yes")
    else:
        print("no")
