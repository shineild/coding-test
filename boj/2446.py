n = int(input())
s = 0
for i in range(1, 2*n,2):
    print(" "*s+"*"*(2*n-i))
    s += 1
s -= 1
for i in range(2*n-3,0, -2):
    s -= 1
    print(" "*s+"*"*(2*n-i))
