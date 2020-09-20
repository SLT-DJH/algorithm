class Solution :
    def isPalindrome(self, x) :
        come = str(x)

        setting = ''

        last = len(come)

        for i in range(last) :
            setting += come[last-1-i]

        if come == setting :
            return True
        else :
            return False

number = int(input())

a = Solution()

b = a.isPalindrome(number)

print(b)
            
