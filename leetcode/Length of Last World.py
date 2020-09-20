class Solution:
    def lengthOfLastWord(self, s):
        get = s.split()

        if get == [] :
            return 0
        else :
            return len(get[len(get)-1])



s = ""

a = Solution()
b = a.lengthOfLastWord(s)

print(b)
