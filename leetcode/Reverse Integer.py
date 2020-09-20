class Solution :
    def reverse(self, x) :
        come = str(x)
        
        minus = ''
        temp = ''

        if come[0] == '-' :
            minus += come[0]
            come = come[1:]

        for i in range(len(come)) :
            temp += come[len(come) -1 -i]

        answer = minus + temp

        answer = int(answer)

        if answer < 0 :
            if answer < -2 ** 31 :
                return 0
            else :
                return answer
        else :
            if answer > 2 ** 31 - 1 :
                return 0
            else :
                return answer

what = int(input())

a = Solution()
b = a.reverse(what)

print(b)
                
