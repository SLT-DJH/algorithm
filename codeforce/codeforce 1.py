n = int(input())

a = []
b = []
c = []

for i in range(3) :
    if i == 0 : 
        line = list(map(int, input().split()))

        a = line
    elif i == 1 :
        line = list(map(int, input().split()))

        b = line
    elif i == 2 :
        line = list(map(int, input().split()))

        c = line

answer = [0 for _ in range(n)]

for i in range(n) :
    geta = a[i]
    getb = b[i]
    getc = c[i]

    if i == 0 :
        answer[i] = geta
    elif i == n-1 :
        if geta != answer[0] and geta != answer[i-1]:
            answer[i] = geta
        elif getb != answer[0] and getb != answer[i-1] :
            answer[i] = getb
        else :
            answer[i] = getc
    else :
        if geta != answer[i-1] :
            answer[i] = geta
        elif getb != answer[i-1] :
            answer[i] = getb
        else :
            answer[i] = getc

print(answer)
