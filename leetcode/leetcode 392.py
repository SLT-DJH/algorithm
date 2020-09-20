class Solution :
    def isSubsequence(self, s, t) :
        start = -1

        check = [0] * len(s)

        for i in range(len(s)) :
            for j in range(start + 1, len(t)) :
                if s[i] == t[j] :
                    start = j
                    check[i] = 1
                    break

        if sum(check) == len(s) :
            return True
        else :
            return False



s = "abc"
t = "ahbgdc"

a = Solution()
b = a.isSubsequence(s, t)
print(b)
