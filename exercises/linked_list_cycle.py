#https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        pos = 0
        def helper(head: Optional[ListNode], seen) -> bool:
            if head is None:
                return False
            else:
                if head not in seen:
                    seen[head] = pos
                    return helper(head.next, seen)
                else:
                    return True
        return helper(head, seen)
        