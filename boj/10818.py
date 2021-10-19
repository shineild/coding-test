n = int(input())
buf = input()
li = list(buf.split())
m = int(li[0])
M = int(li[0])
for i in range(1, n):
    if m > int(li[i]):
        m = int(li[i])
    if M < int(li[i]):
        M = int(li[i])
print(m, M)
