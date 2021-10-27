# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # my first attemps: i think this is n * k, worst case n*n
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        current = head
        count = 0
        while current:
            count +=1
            print(count)
            current = current.next
        
        def rotate(head):
            current = head
            n = current.next
            while n.next is not None:
                current = n
                n = n.next
            current.next = None
            n.next = head
            return n
        
        for _ in range(k % count):
            head = rotate(head)
        return head
    