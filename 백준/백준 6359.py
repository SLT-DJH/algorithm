def open(n) :
    start = 1
    
    box = [0 for _ in range(n+1)]
    
    while start <= n :
        for i in range(start, len(box)) :
            if i % start == 0 :
                if box[i] == 0 :
                    box[i] = 1
                else :
                    box[i] = 0
        start += 1
    return sum(box)

t = int(input())

for _ in range(t) :
    n = int(input())
    
    print(open(n))
