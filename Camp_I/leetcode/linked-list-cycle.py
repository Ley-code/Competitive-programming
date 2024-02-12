# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabit = head
        tort = head
        while rabit and rabit.next:
            rabit = rabit.next.next
            tort = tort.next
            if tort==rabit:
                return True
        if rabit == tort == head:
            return False
        return False