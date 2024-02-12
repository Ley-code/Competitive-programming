# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prevv = None
        prev = None
        while curr:
            prev = curr
            curr = curr.next
            prev.next = prevv
            prevv = prev
        return prev
            