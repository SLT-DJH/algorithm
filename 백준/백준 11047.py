get = input()
get = list(map(int, get.split()))

N = get[0]
K = get[1]

box = []

for _ in range(N) :
    money = int(input())

    box.append(money)

box.sort()
box.reverse()

count = 0

while K != 0 :
    money = 0
    
    for i in range(len(box)) :
        if i == 0 :
            if K >= box[i] :
                money = box[i]
                break
        else :
            if K < box[i-1] and K >= box[i] :
                money = box[i]
                break

    tempcount = K // money
    K = K - (tempcount * money)
    count += tempcount

print(count)
