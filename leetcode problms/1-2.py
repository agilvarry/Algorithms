# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        my first attempt, tweaked to look aa bit better based on the source from betterRotate.
        i think this is n * k, worst case n*n
        """
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


    def betterRotate(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        in this solution we turn the list into a continuous loop
        then we find the item that should be the last, and set it's next->None
        found the idea from: https://www.youtube.com/watch?v=fqZYZK3OCXQ
        """
        if not head or k == 0:
            return head
        
        last = head
        count = 1
        while last.next:
            count +=1
            last = last.next

        last.next = head
        k = count- (k % count)-1
        current = head

        while k >0:
            current = current.next
            k=k-1
        r = current.next
        current.next= None
        return r