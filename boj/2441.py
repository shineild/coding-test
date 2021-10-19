a = int(input())
for b in range(a, 0, -1):
    print(' ' * (a-b) + '*' * b)
