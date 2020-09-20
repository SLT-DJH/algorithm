def prime(num) :
    i = 2
    while i * i <= num :
        if num % i == 0 :
            return False
        i += 1
    return True


what = input()

what = list(map(int, what.split()))

M = what[0]
N = what[1]

for i in range(M, N+1) :
    if(prime(i)) :
        print(i)


