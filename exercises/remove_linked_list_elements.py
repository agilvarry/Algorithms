#https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        init = ListNode(-1)
        top = init
        
        while head:
            if head.val != val:
                top.next = head
                top = top.next
            head = head.next
        top.next = None #clears the last item in case it was val
        return init.next