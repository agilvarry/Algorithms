#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        queue = collections.deque([root])
        while(queue):
            l = len(queue)
            for i in (range(l)):
                n = queue.popleft()
                if i <l-1: #stops from making connection with next level, leaves rightmost.next = None
                      n.next = queue[0]
                if n.left:
                      queue.append(n.left)
                if n.right:
                      queue.append(n.right)
        return root
                      