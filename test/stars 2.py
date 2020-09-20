number = int(input())

star = '*'
blank= ' '

for i in range(number) :
    answer = (blank * i) + (star * (2*(number-i)-1))
    print(answer)

for i in range(1, number) :
    answer = (blank * (number - 1 - i)) + (star * (2*i + 1))
    print(answer)
