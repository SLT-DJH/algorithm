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
    

t = int(input())

for _ in range(t) :
    n, k = map(int, input().split())

    result = input()

    wcount = result.count("W")

    if wcount == 0 :
        if k != 0 :
            print((2*k) -1)
        else :
            print(0)
    else :
        score = getsum(result)

        betL = []
        nobetL = []

        start = -1
        end = -1

        tempw = 0

        count = 0

        for i in range(len(result)) :

            if result[i] == "L" :
                count += 1
            else :
                tempw += 1
                
                if start == -1 and end == -1 :
                    if count != 0 :
                        nobetL.append(count)
                    count = 0
                    start = i
                elif start != -1 and end == -1 and tempw != wcount:
                    if count != 0 :
                        betL.append(count)
                    count = 0
                elif start != -1 and end == -1 and tempw == wcount :
                    if count != 0 :
                        betL.append(count)
                    count = 0
                    end = i
        if count != 0 :
            nobetL.append(count)

        betL = sorted(betL)
        nobetL = sorted(nobetL)

        tempsum = 0

        if sum(betL) >= k :
            for i in betL :
                if k >= i :
                    tempsum += (2*i) + 1
                    k -= i
                else :
                    tempsum += (2*k)
                    break
            print(score + tempsum)
        else :
            for i in betL :
                if k >= i :
                    tempsum += (2*i) + 1
                    k -= i
                else :
                    tempsum += (2*k)
                    break

            for i in nobetL :
                if k >= i :
                    tempsum += (2*i)
                    k -= i
                else :
                    tempsum += (2*k)
                    break
                
            print(score + tempsum)
                
                    

        
