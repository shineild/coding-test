x = input()
y = x.split()
for n in range(0, len(y)):
    print(y[n])
    if y[n] == 'q':
        break;
