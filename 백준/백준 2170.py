N = int(input())

box = []

for _ in range(N) :
    a, b = map(int, input().split())
  
    box.append([a, b])

box.sort(key = lambda x: (x[0], -x[1]))

answer = 0

mini = 0
maxi = 0

if N == 1 :
    print(box[0][1] - box[0][0])
else :

    for i in range(N) :
        
        if i == 0 :  
            mini = box[i][0]
            maxi = box[i][1]
        elif i == N-1 :
            if mini <= box[i][0] <= maxi :
                if box[i][1] > maxi :
                    maxi = box[i][1]
            else :
                answer += maxi - mini
                mini = box[i][0]
                maxi = box[i][1]
        
            answer += maxi - mini
        else :
            if mini <= box[i][0] <= maxi :
                if box[i][1] > maxi :
                    maxi = box[i][1]
            else :
                answer += maxi - mini
                mini = box[i][0]
                maxi = box[i][1]

    print(answer)
