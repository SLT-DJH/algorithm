def distance(pox, poy) :
    x = (pox[0] - poy[0]) ** 2
    y = (pox[1] - poy[1]) ** 2

    z = x + y

    return z
    

class Solution:
    def numberOfBoomerangs(self, points) :

        x = points[0]
        y = points[1]
        z = points[2]

        a = distance(x,y)
        b = distance(y,z)
        c = distance(x,z)

        check = [a,b,c]

        
        if len(set(check)) == 2 :
            return 2
        elif len(set(check)) == 3 :
            return 0

        




points = [[0,0],[1,0],[2,0]]

a = Solution()
b = a.numberOfBoomerangs(points)
print(b)
