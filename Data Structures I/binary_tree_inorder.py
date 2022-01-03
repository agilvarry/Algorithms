#https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        
        if root is None:
            return inorder
        
        def traverse(root:Optional[TreeNode]):
            if root.left:
                traverse(root.left)
            inorder.append(root.val)
            if root.right:
                traverse(root.right)           
            
        traverse(root)
        return inorder