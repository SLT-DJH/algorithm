def prime(a) :
    if a <= 1 :
        return False
    elif a == 2 :
        return True
    elif a == 3 :
        return True
    else :
        i = 2

        while i * i <= a :
            if a % i == 0 :
                return False
            else :
                i += 1

        return True

box = [0 for _ in range((123456 * 2) + 1)]

for i in range(len(box)) :
    if prime(i) :
        box[i] = 1


while True :
    n = int(input())

    if n == 0 :
        break
    else :
        doublen = 2 * n

        count = 0

        for i in range(n + 1, doublen + 1) :
            if box[i] == 1 :
                count += 1

        print(count)
