#https://leetcode.com/problems/validate-binary-search-tree/

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:               
        return self.recurse(root, float('-inf'), float('inf'))
    
    def recurse(self,  root, minV, maxV):
        if root is None:
            return True
        elif root.val <= minV or root.val >= maxV:
            return False
        else:
            return self.recurse(root.left, minV, root.val) and self.recurse(root.right, root.val, maxV)