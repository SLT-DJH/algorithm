def prime(a) :
    if a == 1 :
        return False
    elif a == 2 :
        return True
    elif a == 3 :
        return True
    else :
        check = 2

        while check * check <= a :
            if a % check == 0 :
                return False
            else :
                check += 1

        return True

T = int(input())

box = []

for i in range(1, 10001) :
    if prime(i) :
        box.append(i)

for i in range(T) :
    n = int(input())
    start = 0
    count = 0

    for i in box :
        if start == 0 and i >= n // 2 :
            start = box.index(i)

    for i in range(start, len(box)-1) :
        if count != 0 :
            break
        check = n - box[i]
        if prime(check) :
            if box[i] >= check :
                print(check, box[i])
                count += 1
            else :
                print(box[i], check)
                count += 1
    
