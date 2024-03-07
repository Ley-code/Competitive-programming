# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle  = head
        idx = 0
        while head:
            if idx%2==1:
                middle = middle.next
            head = head.next
            idx+=1
        return middle