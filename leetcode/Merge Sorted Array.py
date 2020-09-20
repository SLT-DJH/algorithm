class Solution:
    def merge(self, nums1, m, nums2, n) :

        for i in range(n) :
            nums1.remove(0)
        
        for i in range(n) :
            nums1.append(nums2[i])

        nums1.sort()


nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
nums2 = [1,2,2]

a = Solution()
b = a.merge(nums1, 6, nums2, 3)

print(nums1)
