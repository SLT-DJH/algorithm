class Solution:
    def maxSubArray(self, nums):

        count = 0

        maximum = 0

        sums = []

        for i in nums :
            if count == 0 :
                maximum = i
                count += 1

                sums.append(maximum)
            else :
                if maximum + i > i :
                    maximum = maximum + i
                    sums.append(maximum)
                else :
                    maximum = i
                    sums.append(maximum)


        return max(sums)
        



nums = [1]
a = Solution()
b = a.maxSubArray(nums)

print(b)
