# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length+=1
        idx = length//2
        curr = head
        while curr and idx>0:
            curr = curr.next
            idx-=1
        return curr
