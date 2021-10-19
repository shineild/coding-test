n = int(input())
for i in range(n):
    q = list(input())
    cnt = 0
    s = 0
    for j in range(len(q)):
        if q[j] == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0
    print(s)
