#https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = None
        def helper(head, lst):
            if head is None:
                return lst
            else:
                copy = head
                head=head.next
                copy.next=lst
                return helper(head, copy)
        return helper(head,lst)