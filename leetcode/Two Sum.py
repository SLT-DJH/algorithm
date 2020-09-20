class Solution :
    def twoSum(self, nums, target) :

        total = 0
        
        for i in range(len(nums)) :
            for j in range(i, len(nums)) :
                total = nums[i] + nums[j]
                if total == target :
                    answer = [i,j]
                    return answer

a = Solution()

b = a.twoSum([2,7,11,15] , 9)

print(b)
