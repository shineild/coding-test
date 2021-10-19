n = input()
l = n.split()
i = len(l)
for k in range(0, i):
    print(l[k])
    if l[k] == '0':
        break
