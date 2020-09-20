class Solution:

    def test(self, root, box) :

        box.append(root)

        if root != 3 :
            self.test(root+1, box)
        
    
    def levelOrderBottom(self, root) :

        box = []

        self.test(root, box)


        return box




a = Solution()
b = a.levelOrderBottom(1)
