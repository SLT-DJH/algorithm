class Solution:
    def countAndSay(self, n: int) -> str:
        count = n
        
        answer = "1"

        numcount = 0

        check = ""
    
        temp = ""
        
        while count != 1 :

            for i in range(len(answer)) :
                if i != len(answer) - 1 :
                    
                    if check == "" :
                        check = answer[i]
                        numcount += 1
                    else :
                        if answer[i] == check :
                            numcount += 1
                        else :
                            temp += str(numcount)
                            temp += check

                            check = answer[i]
                            numcount = 1
                else :
                    if check == "" :
                        check = answer[i]
                        numcount += 1

                        temp += str(numcount)
                        temp += check
                    else :
                        if answer[i] == check :
                            numcount += 1

                            temp += str(numcount)
                            temp += check
                        else :
                            temp += str(numcount)
                            temp += check

                            check = answer[i]
                            numcount = 1

                            temp += str(numcount)
                            temp += check
            numcount = 0
            check = ""
            answer = temp
            temp = ""

            count = count - 1
        
        return answer


a = Solution()
b = a.countAndSay(6)

print(b)
