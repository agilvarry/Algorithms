#https://leetcode.com/problems/binary-tree-postorder-traversal/
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        
        if root is None:
            return postorder
        
        def traverse(root:Optional[TreeNode]):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            postorder.append(root.val)
            
        traverse(root)
        return postorder