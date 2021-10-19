import sys


arr = [[] for _ in range(201)]

n = int(sys.stdin.readline())

for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    arr[age].append(name)
for i in range(len(arr)):
    if len(arr[i]) > 0:
        for k in arr[i]:
            print(i, k)
