#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen={}
        init = ListNode(-1)
        top = init
        while head:
            if head.val not in seen:
                seen[head.val] = 1
                top.next=head
                top=top.next
            head=head.next
        top.next=None
        return init.next
        