def numtobit(num) :
    bit = []
    
    while num != 0 :
        bit.append(num % 2)
        
        num = num // 2
    
    return bit

def bittonum(numlist) :
    num = 0
    
    for i in range(len(numlist)) :
        num += numlist[i] * (2 ** i)
    
    return num

class Solution:
    def findComplement(self, num):
        if num == 0 :
            return 1
        
        k = numtobit(num)

        for i in range(len(k)) :
            if k[i] == 0 :
                k[i] = 1
            else :
                k[i] = 0
        
        l = bittonum(k)

        return l


num = 5

a = Solution()
b = a.findComplement(num)
print(b)
        
