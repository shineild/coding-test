s = input()
s = list(s)
l = len(s)
for i in range(97, 123):
    check = -1
    for j in range(l):
        if chr(i) == s[j]:
            print(j, end=" ")
            check = 0
            break
    if check == -1:
        print(check, end=" ")
