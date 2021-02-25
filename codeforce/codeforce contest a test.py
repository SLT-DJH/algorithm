def getsum(result) :
    answer = 0

    box = []

    count = 0
    
    for i in result :
        if i == "W" :
            count += 1
        else :
            box.append(count)
            count = 0

    box.append(count)

    for i in box :
        if i != 0 :
            answer += (2 * i) - 1

    return answer
