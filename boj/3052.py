cnt = 0
ch = []
for i in range(10):
    n = int(input())
    d = n % 42
    ch.append(d)
for i in range(10):
    tmp = 0
    for j in range(i+1, 10):
        if ch[i] == ch[j]:
            tmp += 1
    if tmp == 0:
        cnt += 1
print(cnt)
