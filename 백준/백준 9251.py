A = input()
B = input()

count = 0

answer = []

checkstart = 0
start = 0

while checkstart != len(A) :

    for i in range(checkstart, len(A)) :
        check = A[i]

        for j in range(start, len(B)) :
            if B[j] == check :
                start = j

                count += 1
                break
            
    answer.append(count)
    count = 0
    start = 0
    checkstart += 1

print(max(answer))

    
