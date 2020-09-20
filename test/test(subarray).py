a = [1, 2, 3, 4, 5]

start = len(a)

box = []

while start != 0 :
    temp = []

    get = start

    for i in range(len(a)) :
        if i <= len(a) - start :
            while get != 0 :
                temp.append(a[i+get-1])

                get = get - 1
            box.append(temp)
            temp = []

            get = start

    start = start - 1

print(box)
