def getbi(num) :
    answer = ""

    while num != 0 :
        answer += str(num % 2)

        num = num // 2

    return answer[::-1]

def check(bi) :
    for i in range(1, len(bi)) :
        
        if bi[i] == "1" :
            if bi[i-1] == "1" :
                return False

    return True

while True :

    N = int(input())

    start = 0
    end = 0

    for i in range(N) :
        if i != N-1 :
            start += 1 * (2**i)
            end += 1 * (2**i)
        else :
            start += 1 * (2 **i)

    end += 1
    start += 1

    count = 0

    for i in range(end, start) :
        a = getbi(i)
        if check(a) :
            print(a)
            count += 1

    print(count)

## dp로 풀 수 있음!
