#https://leetcode.com/problems/binary-tree-level-order-traversal/
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = []
        if not root:
            return order
        queue = collections.deque([root])
        while queue:
            row=[]
            l = len(queue)
            for i in range(l):
                n = queue.popleft()
                row.append(n.val)
                if n.left:
                      queue.append(n.left)
                if n.right:
                      queue.append(n.right)
            order.append(row)
        return order