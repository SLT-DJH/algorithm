number = int(input())

stars = ''

for i in range(number) :
    stars += '*'
    print(stars)

for i in range(number -1) :
    stars = stars[:number-1-i]
    print(stars)
