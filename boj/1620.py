import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
li = []
for i in range(n):
    li.append(sys.stdin.readline().rstrip())
    dic[li[i]] = i+1
for i in range(m):
    tmp = sys.stdin.readline().rstrip()
    if tmp.isdigit():
        print(li[int(tmp)-1])
    else:
        print(dic[tmp])
