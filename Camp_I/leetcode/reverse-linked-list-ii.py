# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            prevv = None
            prev = None
            while curr:
                prev = curr
                curr = curr.next
                prev.next = prevv
                prevv = prev
            return prev
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        n = left-1
        while n>0:
            curr = curr.next
            n-=1
        follow = dummy
        m  = right
        while m>0:
            follow = follow.next
            m-=1
        tail = follow.next
        follow.next = None
        headR = curr.next
        curr.next = None
        curr.next = reverseList(headR)
        headR.next = tail
        return dummy.next
        
        

        
        

