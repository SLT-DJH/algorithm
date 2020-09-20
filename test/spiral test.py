matrix = [[1,2,3,4, 5],[6,7,8,9,10],[11,12, 13, 14, 15],[16,17,18,19,20],[21,22,23,24,25]]

allnum = len(matrix) * len(matrix[0])

answer = []

start = 0
endcount = len(matrix[0])
end = len(matrix)
        
while True :
    if len(answer) == (allnum) :
        break
    
    for i in range(start, endcount) :
        if i != endcount-1 :  
            answer.append(matrix[start][i])
            if len(answer) == (allnum) :
                break
        else :
            if len(answer) == (allnum-1) :
                answer.append(matrix[start][i])
                print("1", answer)
                break
            else :
                for j in range(start, end) :
                    if j != end-1 :
                        answer.append(matrix[j][i])
                        if len(answer) == (allnum) :
                            print("2", answer)
                            break
                    else :
                        if len(answer) == (allnum-1) :
                            answer.append(matrix[j][i])
                            print("2", answer)
                            break
                        else :
                            for k in range(start, endcount) :
                                if k != endcount-1 :
                                    answer.append(matrix[j][endcount - 1 - k + start])
                                    if len(answer) == (allnum) :
                                        print("3", answer)
                                        break
                                else :
                                    if len(answer) == (allnum-1) :
                                        answer.append(matrix[j][endcount-1- k + start])
                                        print("3", answer)
                                        break
                                    else :
                                        for l in range(start, end-1) :
                                            answer.append(matrix[end-1-l+start][start])
                                            if len(answer) == (allnum) :
                                                print("4", answer)
                                                break
    start += 1
    end = end - 1
    endcount = endcount - 1

print(answer)
