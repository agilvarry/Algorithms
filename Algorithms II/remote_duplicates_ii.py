# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen={}
        init = ListNode(-1)
        top = init
     
        while head:
            if head.next and head.val == head.next.val:
                seen[head.val] = 1
            if head.val not in seen:
                top.next = head
                top=top.next
                    
            head=head.next
        top.next=None
        return init.next
            