# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode(None)
        dummynode.next = head
        curr = head
        while curr and curr.next:
            while curr and curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
                
            curr = curr.next
        return dummynode.next

