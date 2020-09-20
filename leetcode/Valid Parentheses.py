class Solution :
    def isValid(self, s) :

        left = []

        for i in s :
            if i == '(' or i == '[' or i == '{' :
                left.append(i)
            else :
                if left == [] :
                    return False
                else :
                    check = left.pop()

                    if i == ')' :
                        if check != '(' :
                            return False
                    elif i == ']' :
                        if check != '[' :
                            return False
                    else :
                        if check != '{' :
                            return False

        if left == [] :
            return True
        else :
            return False


a = Solution()
b = a.isValid("]")
print(b)
