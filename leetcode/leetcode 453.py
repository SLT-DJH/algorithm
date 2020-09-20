class Solution:
    def minMoves(self, nums):
        count = 0
        temp = len(nums) - 1
        maxnum = max(nums)
        
        while True :
            change = temp
            
            getmax = maxnum
            
            for i in range(len(nums)) :
                if change != 0 :
                    if nums[i] < maxnum :
                        nums[i] = nums[i] + 1
                        change = change - 1
            
            if change != 0 :
                for i in range(len(nums)) :
                    if change != 0 :
                        if nums[i] == maxnum :
                            nums[i] = nums[i] + 1
                            change = change - 1

            print(nums)
            
            tempmax = max(nums)
            
            if tempmax != maxnum :
                maxnum = tempmax

            count += 1
            
            getset = set(nums)
            
            if len(getset) == 1 :
                break
        
        return count


nums = [1,2,3,4,5]
a = Solution()
b = a.minMoves(nums)

print(b)
