R, G, B = map(int, input().split())
r = 0
g = 0
b = 0
cnt = 0
while (r<R):
    print(r, g, b)
    cnt += 1
    if b < B-1:
        b += 1
    else:
        b = 0
        g += 1
        if g == G:
            g = 0
            r += 1
print(cnt)
