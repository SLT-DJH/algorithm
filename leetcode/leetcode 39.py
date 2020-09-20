def DFS(candi, target, final, candidates) :
    
    if sum(candi) == target :
        final.append(sorted(candi[:]))
        return
    
    for i in candidates :
        check = candi + [i]
        if sum(check) <= target:
            candi.append(i)
            DFS(candi, target, final, candidates)
            candi.pop()

class Solution:
    def combinationSum(self, candidates, target) :
        final = []
        
        DFS([], target, final, candidates)

        answer = []

        for i in final :
            if i not in answer :
                answer.append(i)
        
        return answer

candidates = [2,3,5]
target = 8


a = Solution()
b = a.combinationSum(candidates, target)

print(b)
