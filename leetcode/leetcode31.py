from itertools import permutations

class Solution:
    def nextPermutation(self, nums):
        get = sorted(nums)
        
        answer = list(permutations(get,len(get)))

        take = []

        for i in answer :
            if i not in take :
                take.append(i)

        print(take)

        
        for i in range(len(take)) :
            if i != len(take) -1 :
                if nums == list(take[i]) :
                    for j in range(len(nums)) :
                        temp = list(take[i+1])
                        nums[j] = temp[j]

                    break
            else :
                for j in range(len(nums)) :
                    nums[j] = get[j]


nums = [1,5,1]

a = Solution()

b = a.nextPermutation(nums)

print(nums)
