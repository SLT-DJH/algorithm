class Solution:
    def removeElements(self, head, val) :
        answer = []

        for i in head :
            if i != val :
                answer.append(i)

        return answer


head = [1,2,6,3,4,5,6]
val = 6

a = Solution()
b = a.removeElements(head, val)

print(b)
