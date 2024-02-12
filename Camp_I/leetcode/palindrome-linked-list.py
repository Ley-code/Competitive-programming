# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        prev = ListNode()
        while curr:
            temp = ListNode(curr.val)
            temp.next = prev
            prev = temp
            curr = curr.next
        curr = head
        while curr:
            if curr.val!=prev.val:
                return False
            curr = curr.next
            prev = prev.next
        return True