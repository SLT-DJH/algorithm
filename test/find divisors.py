def findDivisor(num) :
    divisor = [1]
    answer = [1]
    
    i = 2

    while i ** 2 <= num :
        if num % i == 0 :
            divisor.append(i)
            answer.append(i)
        i += 1
    for j in divisor :
        if j != 1 :
            answer.append(num//j)

    return sum(answer)
        
