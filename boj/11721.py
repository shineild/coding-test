a = input(); b = list(a); l = len(b); d = 0
for c in range(0, l):
    d = c + 1
    if d % 10 == 0 and c != 1:
        print(b[c])
    else:
        print(b[c], end='')
