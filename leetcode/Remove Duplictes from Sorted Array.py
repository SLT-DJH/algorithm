class Solution:
    def removeDuplicates(self, nums) :
        answer = set(nums)
        answer = list(answer)
        answer.sort()

        for i in range(len(answer)) :
            nums[i] = answer[i]

        return len(answer)


nums = [-1,0,0,0,0,3,3]

a = Solution()
b = a.removeDuplicates(nums)

for i in range(b) :
    print(nums[i])
