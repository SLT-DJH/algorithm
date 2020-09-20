import math

class Solution :
    def calculate(self, s) :
        self.s = s
        s = s.replace(' ', '')
        s = s.replace('"', '')
        temporary = ''
        box = []
        answer = []
        total = 0
        count = 0
        setting = 0
        for i in range(len(s)) :
            if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/' :
                box.append(temporary)
                box.append(s[i])
                temporary = ''
            elif i == len(s) - 1 :
                box.append(temporary + s[i])
            else :
                temporary = temporary + s[i]
        for i in range(len(box)) :
            if box[i] == '/' :
                if box[i-1] == '-1' :
                    box[i-1] = math.trunc(int(box[i-3]) / int(box[i+1]))
                    box[i-1] = str(box[i-1])
                    box[i+1] = '-1'
                else :
                    box[i-1] = math.trunc(int(box[i-1]) / int(box[i+1]))
                    box[i-1] = str(box[i-1])
                    box[i+1] = '-1'
            elif box[i] == '*' :
                if box[i-1] == '-1' :
                    box[i-1] = int(box[i-3]) * int(box[i+1])
                    box[i-1] = str(box[i-1])
                    box[i+1] = '-1'
                    box[i-3] = '-1'
                else :
                    box[i-1] = int(box[i-1]) * int(box[i+1])
                    box[i-1] = str(box[i-1])
                    box[i+1] = '-1'
        for i in range(len(box)) :
            if box[i] != '/' and box[i] != '*' and box[i] != '-1' :
                answer.append(box[i])
        for i in range(len(answer)) :
            if count == 0 :
                total = total + int(answer[i])
                count = count + 1
            elif count % 2 == 1 :
                if answer[i] == '+' :
                    setting = 1
                elif answer[i] == '-' :
                    setting = 2
                count = count + 1
            elif count %2 == 0 :
                if setting == 1 :
                    total = total + int(answer[i])
                elif setting == 2 :
                    total = total - int(answer[i])
                count = count + 1
        return total


a = input()

b = Solution()

print(b.calculate(a))
