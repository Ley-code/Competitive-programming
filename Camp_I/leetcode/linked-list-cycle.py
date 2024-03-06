# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabit = head
        hare = head
        while rabit and rabit.next:
            rabit = rabit.next.next
            hare = hare.next
            if rabit == hare:
                return True
        return False