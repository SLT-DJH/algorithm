class Solution:
    def addBinary(self, a, b):
        if a == "0" and b == "0" :
            return "0"
        else :
            
            alist = []
            blist = []

            anum = 0
            bnum = 0

            for i in a :
                alist.append(str(i))

            for i in b :
                blist.append(str(i))

            acount = len(alist) - 1
            bcount = len(blist) - 1

            for i in alist :
                anum += int(i) * (2 ** acount)

                acount = acount - 1

            for i in blist :
                bnum += int(i) * (2 ** bcount)

                bcount = bcount - 1

            cnum = anum + bnum

            clist = []

            while cnum != 1 :
                clist.append(str(cnum % 2))

                cnum = cnum // 2

            clist.append(str(1))

            answer = ""

            last = len(clist)

            while last != 0 :
                answer += clist[last-1]

                last = last - 1

            return answer

        


a = "1"
b = "0"

k = Solution()
l = k.addBinary(a, b)

print(l)
