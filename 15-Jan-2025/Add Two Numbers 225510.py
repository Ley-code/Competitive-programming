# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode = ListNode()
        curr = ListNode()
        dummynode.next = curr
        
        carry = 0
        while l1 and l2:
            val = (l1.val+l2.val+carry)%10
            carry = (l1.val+l2.val+carry)//10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = (l1.val+carry)%10
            carry = (carry+l1.val)//10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        while l2:
            val = (l2.val+carry)%10
            carry = (l2.val+carry)//10
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummynode.next.next