class Solution :
    def generate(self, rowIndex) :
        getanswer = []

        setlist = []

        temp = []

        for i in range(33) :
                   
            if i == 0 :
                getanswer.append([1])
            else :
                count = i + 1

                for j in range(count) :
                    if j == 0 or j == (count - 1) :
                        temp.append(1)
                    else :
                        temp.append(setlist[j-1] + setlist[j])

                setlist = temp
                temp = []
                getanswer.append(setlist)

        return getanswer[rowIndex]


a = Solution()
b = a.generate(3)

print(b)
