n = int(input())
b = ''
c = ''
for i in range(n):
    if i %2 == 0:
        b += '*'
        c += ' '
    else:
        b += ' '
        c += '*'
for i in range(n):
    print(b)
    print(c)
