burgers = []
beverages = []


for i in range(3) :
    burger = int(input())
    burgers.append(burger)

for i in range(2) :
    beverage = int(input())
    beverages.append(beverage)

print(min(burgers) + min(beverages) - 50)
    
