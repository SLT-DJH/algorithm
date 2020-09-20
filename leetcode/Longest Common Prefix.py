class Solution :
    def longestCommonPrefix(self, strs) :

        for i in strs :
            if i == '' :
                return ''

        count = 0
        standard = ''

        for i in strs :
            if count == 0 :
                standard = i
                count = len(i)
            else :
                if len(i) < count :
                    standard = i
                    count = len(i)
                    
        listcount = len(strs)

        tempcount = 0

        prefix = ''

        for i in range(len(standard)) :
            for j in range(len(strs)) :
                if strs[j][i] == standard[i] :
                    tempcount += 1
            if tempcount == listcount :
                prefix += standard[i]
                tempcount = 0
            else :
                if prefix == '' :
                    return ''
                tempcount = 0
                
        return prefix

a = Solution()
b = a.longestCommonPrefix(["aca", "cba"])
