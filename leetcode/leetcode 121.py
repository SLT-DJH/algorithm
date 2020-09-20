class Solution :
    def maxProfit(self, prices) :
        count = 0
        buy = 0
        sell = 0
        profit = 0

        for i in prices :
            if count == 0 :
                buy = i
                count += 1
            else :
                if i < buy :
                    buy = i
                else :
                    sell = i
                    
                    if profit == 0 :
                        profit = sell - buy
                    else :
                        temp = sell - buy

                        if temp > profit :
                            profit = temp
        
        return profit


prices = [7, 1, 5, 3, 6, 4]

a = Solution()
b = a.maxProfit(prices)

print(b)
