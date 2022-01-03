#https://leetcode.com/problems/binary-tree-preorder-traversal/
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        
        if root is None:
            return preorder
        
        def traverse(root:Optional[TreeNode]):
            preorder.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)           
            
        traverse(root)
        return preorder