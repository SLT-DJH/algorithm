def prime(a, k) :
    if a == 1 or a == 2 or a == 3:
        return a
    else :
        check = 2
        point = 0
        best = 0

        while check * check <= a and check <= k:
            if a % check == 0 :
                point = 1
                temp = a // check

                if temp <= k :
                    return check
                else :
                    best = temp

                check += 1
            else :
                check += 1

        if point == 0 :
            return a
        else :
            return best

t = int(input())

for _ in range(t) :
    n, k = map(int, input().split())

    if n <= k :
        print(1)
    elif k == 1 :
        print(n)
    else :
        print(prime(n, k))
                    
            
