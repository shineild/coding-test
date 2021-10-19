x, y = map(int, input().split())
cal = {1 : "MON", 2 : "TUE", 3 : "WED", 4 : "THU", 5 : "FRI", 6 : "SAT", 7 : "SUN"}
mon = {1 : 1, 2 : 4, 3 : 4, 4 : 7, 5 : 2, 6 : 5, 7 : 7, 8 : 3, 9 : 6, 10 : 1, 11 : 4, 12 : 6}
a = mon[x]
if y == 1:
    print(cal[a])
else:
    for b in range(2, y+1):
        a += 1
        if a == 8:
            a = 1
    print(cal[a])
