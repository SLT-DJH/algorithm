a = int(input())

b = 1000 - a

coin = 0

while b != 0 :
    if b >= 500 :
        coin = coin + 1
        b = b - 500
    elif 100 <= b < 500 :
        coin = coin + 1
        b = b - 100
    elif 50 <= b < 100 :
        coin = coin + 1
        b = b - 50
    elif 10 <= b < 50 :
        coin = coin + 1
        b = b - 10
    elif 5 <= b < 10 :
        coin = coin + 1
        b = b - 5
    else :
        coin = coin + 1
        b = b - 1

print(coin)
