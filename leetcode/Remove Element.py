class Solution:
    def removeElement(self, nums, val) :
        change = 0

        for i in range(len(nums)) :
            if nums[i] != val :
                nums[change] = nums[i]
                change += 1

        return change


nums = [0,1,2,2,3,0,4,2]
val = 2

a = Solution()
b = a.removeElement(nums, val)

for i in range(b) :
    print(nums[i])
