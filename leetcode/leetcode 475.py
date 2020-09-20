class Solution :
    def findRadius(self, houses, heaters) :
        radius = 0

        visited = []
        position = []

        for i in heaters :
            position.append(i)

        count = 0
        
        for i in houses :
            if i in position :
                count +=1

        if count == len(houses) :
            return 0

        while True :
            radius += 1

            for i in position :
                visited.append(i)

            for i in range(len(position)) :
                check = position[i] + radius
                
                if check not in visited and check <= 10 ** 9:
                    visited.append(check)

            for i in range(len(position)) :
                check = position[i] - radius

                if check not in visited and check >= 0 :
                    visited.append(check)

            count = 0

            for i in houses :
                if i in visited :
                    count += 1

            if count == len(houses) :
                return radius
                break
                    


houses = [1,2,3,4,5,8,10,30]
heaters = [13, 50]

a = Solution()
b = a.findRadius(houses, heaters)
print(b)
