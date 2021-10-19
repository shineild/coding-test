a = input()
if a == "0":
    print(1)
    exit()
c = a
x = 0
y = 0
count = 0
if len(a) == 1:
    c = "0" + a
    a = a + a
    count += 1
b = list(map(int, list(a)))
check = list(map(int, list(c)))
while(1):
    x = b[0] + b[1]
    b[0] = b[1]
    if len(str(x)) == 1:
        b[1] = x
    else:
        y = list(map(int, list(str(x))))
        b[1] = y[1]
    count += 1
    if b == check:
        print(count)
        break
