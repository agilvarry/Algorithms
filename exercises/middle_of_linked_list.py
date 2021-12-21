#https://leetcode.com/problems/middle-of-the-linked-list/
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #this one is cool and i did not come up with it
        #move the head by one, and move another pointer by 2
        #when the fast pointer gets to the end you would have 
        #your head at the middle
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        return head
      