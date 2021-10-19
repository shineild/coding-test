import sys

n = int(sys.stdin.readline())
arr = [[] for _ in range(51)]
for i in range(n):
    word = sys.stdin.readline().rstrip()
    l = len(word)
    if word not in arr[l]:
        arr[l].append(word)

for c in arr:
    l = len(c)
    if l > 1:
        c = sorted(c)
        for k in c:
            print(k)
    elif l == 1:
        print(c[0])
