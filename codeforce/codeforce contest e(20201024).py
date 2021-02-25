import math

n = int(input())

a = math.factorial(n)

b = math.factorial(n//2)

c = (a // b) // b

d = math.factorial((n//2) - 1)

e = c * d * d // 2

print(e)
