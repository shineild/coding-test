num = int(input())
buf = input()
array = buf.split()
min = int(array[0])
for i in range(1, num):
    if min > int(array[i]):
        min = int(array[i])
print(min)
