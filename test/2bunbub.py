number = -20
inputlist = [-5, -20, 0, 24, -1, 10]

inputlist.sort()

mini = 0
maxi = len(inputlist) - 1
mid = (mini + maxi) // 2

if number == inputlist[mid] :
    print('있음')
else :
     while mini < mid :
         if number > inputlist[mid] :
            mini = mid
            mid = (mini + maxi) // 2
         elif number < inputlist[mid] :
             maxi = mid
             mid = (mini + maxi) // 2
         else :
               break
     if inputlist[mini] == number or inputlist[maxi] == number or inputlist[mid] == number :
         print('있음')
     else :
         print('없음')
