import sys

t = int(sys.stdin.readline())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    ho = 1

    while(1):
        if h < n:
            n = n - h
            ho += 1

        else:
            floor = n
            if ho < 10:
                print(str(floor) + "0" + str(ho))
                break
            else:
                print(str(floor) + str(ho))
                break
