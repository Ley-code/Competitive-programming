# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode(None)
        greaterthan = ListNode(None)
        dummyless = lessthan
        dummygret = greaterthan
        curr = head
        while curr:
            if curr.val<x:
                lessthan.next = curr
                lessthan = lessthan.next
            else:
                greaterthan.next = curr
                greaterthan = greaterthan.next
            curr = curr.next
        lessthan.next = dummygret.next
        greaterthan.next = None
        return dummyless.next