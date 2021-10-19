c = input()
d = 'a'
while(d != c):
    print(d, end=" ")
    d = chr(ord(d) + 1)
print(c)
