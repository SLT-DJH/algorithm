class Solution:
    def plusOne(self, digits):

        get = ""

        for i in digits :
            get += str(i)

        number = int(get)

        number += 1

        answer = str(number)

        answerlist = []

        for i in answer :
            answerlist.append(int(i))

        return answerlist



digits = [4, 3, 2, 1]

a = Solution()

b = a.plusOne(digits)

print(b)
