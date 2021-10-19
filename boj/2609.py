import sys
import math

a, b = map(int, sys.stdin.readline().split())
c = math.gcd(a, b)
print(c)
print((a*b)//c)

