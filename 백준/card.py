N = int(input())

card = input()
card = list(map(int, card.split()))

best = []

for i in range(N) :
    best.append(card[i])

if len(best) == 1 :
    print(best[0])
else :
    for i in range(1, N) :
        for j in range(1, (i+3) // 2) :
            if best[i] < best[i-j] + best[j-1] :
                best[i] = best[i-j] + best[j-1]
            else :
                continue
    
        

print(best[N-1])
