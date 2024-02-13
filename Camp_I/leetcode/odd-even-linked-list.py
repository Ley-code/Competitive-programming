# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenhead = ListNode()
        oddhead = ListNode()
        dummyeven = evenhead
        dummyodd = oddhead
        curr = head
        idx = 0
        while curr:
            if idx%2==0:
                evenhead.next = curr
                evenhead = evenhead.next
            else:
                oddhead.next = curr
                oddhead = oddhead.next
            curr = curr.next
            idx+=1
        evenhead.next = dummyodd.next
        oddhead.next = None
        return dummyeven.next