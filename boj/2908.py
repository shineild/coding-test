import sys

a, b = map(str, sys.stdin.readline().split())

for i in range(2, -1, -1):
    if a[i] < b[i]:
        c = b
        break
    elif a[i] > b[i]:
        c = a
        break
answer = ""
for i in range(2, -1, -1):
    answer += c[i]

print(answer)
