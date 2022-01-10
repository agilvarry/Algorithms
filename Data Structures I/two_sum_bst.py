#https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return false
        queue = collections.deque([root])
        seen = {}
        
        while queue:
            for i in range(len(queue)):
                n = queue.popleft()
                m = k-n.val
                if m in seen:
                    return True
                else:
                    seen[n.val] = 1
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
        return False