# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head and not head.next:
            return head

        dummyhead = ListNode(None)
        dummyhead.next = head
        lastsorted = head
        curr = head.next
        while curr:
            if curr.val>=lastsorted.val:
                lastsorted = lastsorted.next
            else:
                prev = dummyhead
                while prev.next.val<=curr.val:
                    prev = prev.next
                
                lastsorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastsorted.next
        return dummyhead.next

    