#https://leetcode.com/problems/symmetric-tree/
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(n1: Optional[TreeNode], n2: Optional[TreeNode]):
            if n1 is None and n2 is None:
                return True
            elif n1 is None or n2 is None:
                return False
            return n1.val == n2.val and sym(n1.right, n2.left) and sym(n1.left, n2.right)
        
        return sym(root, root)