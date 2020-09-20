a = list(map(int, input().split()))

count = 0
number = 0

while number < 4 :
  if a[number] == 1 :
        count = count + 1
        number = number + 1
  else :
        number = number + 1
        
if count == 4 :
    print('E')
elif count == 3 :
    print('A')
elif count == 2 :
    print('B')
elif count == 1 :
    print('C')
else :
    print('D')
