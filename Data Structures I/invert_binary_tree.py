#https://leetcode.com/problems/invert-binary-tree/
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root