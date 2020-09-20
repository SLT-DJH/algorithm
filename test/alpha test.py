alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

a = alpha.split()

graph = {}

for i in range(len(a)) :
    graph[a[i]] = i + 1

get = input()

box = []

for i in get :
    box.append(i)

box.reverse()

print(box)

answer = 0

for i in range(len(box)) :
    answer += graph[box[i]] * (26 ** i)
          

print(answer)




