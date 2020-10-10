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
                return check
            else :
                check += 1

        return a
