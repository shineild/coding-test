num = int(input())
i = 1
while (i <= num):
    if i > 2:
        if (i%3 == 0):
            pass
        else:
            print(i, end=" ")
    else:
        print(i, end=" ")
    i += 1
