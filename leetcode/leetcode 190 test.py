a = int(input())

n = int(a)
        
box = []
        
for i in str(n) :
    box.append(i)
        
rebox = box
rebox.reverse()
        
plus = 32 - len(box)
        
for i in range(plus) :
    rebox.append(0)
        
answer = ""
        
for i in rebox :
    answer += str(i)

print(answer)
