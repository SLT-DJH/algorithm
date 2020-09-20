def uclid(numa, numb) :

    if numa <= numb :
        x = numa
        y = numb
    else :
        x = numb
        y = numa

    temp = 0
    
    while y % x != 0 :
        temp = y % x
        y = x
        x = temp

    return x

print(uclid(100, 25))
