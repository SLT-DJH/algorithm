number = int(input())

firstline = '* '
secondline = ' *'

if number == 1 :
    print('*')
else :
    firstanswer = firstline * ((number // 2) + (number % 2))
    secondanswer = secondline * (number // 2)
    for i in range(number) :
        print(firstanswer)
        print(secondanswer)
