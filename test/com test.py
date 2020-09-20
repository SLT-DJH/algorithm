from itertools import permutations

a = [2, 3, 2]


answer = []

for i in range(1,3) :
    get = list(permutations(a)

    for j in get :
        take = sorted(list(j))

        if take not in answer :
            answer.append(take)

print(answer)
