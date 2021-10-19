import sys
import math
n, k = map(int, sys.stdin.readline().split())
f_n = math.factorial(n)
f_k = math.factorial(k)
bottom = f_k * math.factorial(n-k)
print(f_n//bottom)
