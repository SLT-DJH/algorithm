def isValid(k) :
    left = []
    point = []
    
    for i in k :
        if i == "(" :
            left.append(i)
        elif i == ")" :
            if left == [] :
                return False
            else :
                check = left.pop()

                if check != "(" :
                    return False
        elif i == "[" :
            left.append(i)
        elif i == "]" :
            if left == [] :
                return False
            else :
                check = left.pop()

                if check != "[" :
                    return False
        elif i == "." :
            point.append(i)
    
    if left == [] :
        return True
    else :
        return False

inputlist = []

while True :
    get = input()

    if get == "." :
        break

    inputlist.append(get)

for i in inputlist :
    if isValid(i) :
        print('yes')
    else :
        print('no')
