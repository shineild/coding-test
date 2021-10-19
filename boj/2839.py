a=int(input());c=0;
while a > 0:
    if a>4 and a%5 == 0:
        c += a//5
        break
    a -= 3
    c += 1
if a < 0:
    print(-1)
else:
    print(c)
