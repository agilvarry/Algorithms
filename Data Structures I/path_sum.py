#https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        targetSum -= root.val
        
        if root.left is None and root.right is None:
            return targetSum == 0
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)
        