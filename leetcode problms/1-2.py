#https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def frontToBack(head: Optional[ListNode]):
            def iter(head: Optional[ListNode]):
                
                next = head.next
                if next.next is None:
                    head.next = None
                    return head, next
                else:
                    head, next = iter(next)
                return head, next  
            
            head, next = iter(head)
            next.next = head
            print(head)
            
            return next
                
        if k > 0:
            head = frontToBack(head)
            k = k-1
        return head    
        