# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        hare = head
        tort = head
        proceed = False
        while hare and hare.next:
            hare = hare.next.next
            tort = tort.next
            if hare == tort:
                proceed = True
                break
        if not proceed:
            return
        hare = head
        while hare:
            if hare == tort:
                return hare
            hare = hare.next
            tort = tort.next
