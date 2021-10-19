n = input()
n = n.split()
if int(n[0]) - int(n[1]) == -1:
    a = 0
    for i in range(1, 7):
        if int(n[i]) - int(n[i+1]) != -1:
            a = 1
            print("mixed")
            break
    if a == 0:
        print("ascending")
elif int(n[0]) - int(n[1]) == 1:
    a = 0
    for i in range(1, 7):
        if int(n[i]) - int(n[i+1]) != 1:
            a = 1
            print("mixed")
            break
    if a == 0:
        print("descending")
else:
    print("mixed")
