#
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init = ListNode(-1)
        top = init
        i, count = 0,0
        counter = head
        while counter:
            count+=1
            counter = counter.next
        count = count-n
        while head:
            if i != count:
                top.next = head
                top = top.next
            head = head.next
            i+=1
        top.next = None
        return init.next