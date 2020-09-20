class Solution :
    def romanToInt(self, s) :
        roman = {'O' : 0, 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        box = []

        total = 0

        for i in range(len(s)) :
            if s[i] == '"' :
                continue
            else :
                box.append(s[i])

        for i in range(len(box)) :
            if i != len(box) - 1 :
                if roman[box[i]] < roman[box[i+1]] and roman[box[i]] != 0:
                    total += (roman[box[i+1]] - roman[box[i]])
                    box[i+1] = 'O'
                else :
                    total += roman[box[i]]
            else :
                total += roman[box[i]]

        return total


what = input()

a = Solution()

b = a.romanToInt(what)

print(b)
