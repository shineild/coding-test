import sys
dic = {}
for i in range(int(sys.stdin.readline())):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        dic[name] = True
    else:
        del dic[name]
print("\n".join(sorted(dic.keys(), reverse=True)))
