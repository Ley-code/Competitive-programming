#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        curr = head
        while n>0:
            curr = curr.next
            n-=1
        follow = dummy      
        while curr:
            curr = curr.next
            follow = follow.next
        follow.next = follow.next.next
        return dummy.next