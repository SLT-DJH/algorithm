import math

class Solution :
    def calculate(self, s) :
        self.s = s
        s = s.replace(' ', '')
        s = s.replace('"', '')
        temporary = ''
        box = []
        total = 0

        left = []
        
        start = 0
        end = 0
        for i in range(len(s)) :
            if s[i] == '+' or s[i] == '-' or s[i] == ')':
                if s[i-1] == ')' :
                    box.append(s[i])
                    temporary = ''
                else :
                    box.append(temporary)
                    box.append(s[i])
                    temporary = ''
            elif i == len(s) - 1 :
                box.append(temporary + s[i])
            elif s[i] == '(' :
                box.append(s[i])
            else :
                temporary = temporary + s[i]
        for i in range(len(box)) :
            if box[i] == '(' :
                left.append(i)
            if box[i] == ')' :
                start = left.pop()
                end = i
                semitotal = 0

                for j in range(start + 1, end) :
                    if j == start + 1 :
                        semitotal = semitotal + int(box[j])
                    
                    if box[j] == '0' :
                        continue
                    else :
                        if box[j] == '+' :
                            semitotal = semitotal + int(box[j+1])
                        elif box[j] == '-' :
                            semitotal = semitotal - int(box[j+1])

                box[start] = str(semitotal)
                
                for j in range(start + 1, end + 1) :
                    box[j] = str(0)

        for i in range(len(box)) :
            if i == 0 :
                total = total + int(box[i])
            if box[i] == '0' :
                continue
            else :
                if box[i] == '+' :
                    total = total + int(box[i+1])
                elif box[i] == '-' :
                    total = total - int(box[i+1])
        return total
            

a = input()

b = Solution()

print(b.calculate(a))
