def ans(number, time) :
    if time == 1 :
        return number
    elif time % 2 == 1 :
        return ans(number, time - 1) * number
    else :
        number = number * number
        time = time / 2
        return ans(number, time)
