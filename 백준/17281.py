from itertools import permutations

def score(k) :
    global N
    
    outcount = 0

    out = 0

    score = 0

    inning = 0

    start = 0

    b1, b2, b3 = 0, 0, 0

    while True :
        for i in range(start, 9) :
            if i < 3 :
                a = grade[inning][k[i]]
            elif i == 3 :
                a = grade[inning][0]
            else :
                a = grade[inning][k[i-1]]

            if a == 0 :
                out += 1
                
            elif a == 1 :
                
                score += b3
                b1, b2, b3 = 1, b1, b2
                
            elif a == 2 :

                score += b3
                score += b2
                b1, b2, b3 = 0, 1, b1
                
            elif a == 3 :

                score += b3
                score += b2
                score += b1
                b1, b2, b3 = 0, 0, 1
                
            else :

                score += b3
                score += b2
                score += b1
                score += 1

                b1, b2, b3 = 0, 0, 0
                
            start = 0
                
            if out == 3 :
                inning += 1
                start = i + 1
                b1, b2, b3 = 0, 0, 0
                out = 0                
                break
        if inning == N :
            break
        
    return score


N = int(input())

grade = []

best = 0

for i in range(N) :
    numbers = input()
    numbers = list(map(int, numbers.split()))

    grade.append(numbers)

print(grade)

team = [1, 2, 3, 4, 5, 6, 7, 8]

permu = permutations(team, 8)

permu = list(permu)

del permu[100:]

count = 0

for i in permu :
    count += 1
    if best == 0 :
        best = score(i)
    else :
        if best >= score(i) :
            continue
        else :
            best = score(i)
    print(count)
print(best)

    

