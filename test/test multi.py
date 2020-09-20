def calcul(current, numlist) :
    temp = 0

    for i in range(len(numlist)) :
        if i == 0 :
            temp = numlist[0]
        else :
            tempget = current[i-1]
            if tempget == "+" :
                temp = temp + numlist[i]
            elif tempget == "-" :
                temp = temp - numlist[i]
            elif tempget == "x" :
                temp = temp * numlist[i]
            elif tempget == "/" :
                temp = temp // numlist[i]

    return temp
