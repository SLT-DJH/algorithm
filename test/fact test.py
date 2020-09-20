from math import factorial

a = [0 for _ in range(20)]

a[1] = 1

for i in range(2, len(a)) :
    a[i] = (a[i-1] * i) % 1000000007
    
n, k = map(int, input().split())

answer = (a[n] // (a[k] * a[n-k])) % 1000000007

print(answer)
