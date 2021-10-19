n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    a = int(a)
    b = list(b)
    l = len(b)
    for j in range(l):
        print(b[j] * a, end="")
    print("")
