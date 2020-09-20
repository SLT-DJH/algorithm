a = int(input())

memo = [0 for _ in range(1000001)]

memo[0] = 1
memo[1] = 1
memo[2] = 2

for i in range(3, 1000001) :
    memo[i] = memo[i-1] % 1000000009+ memo[i-2] % 1000000009+ memo[i-3] % 1000000009



for i in range(a) :
    b = int(input())
    print(memo[b])
    
