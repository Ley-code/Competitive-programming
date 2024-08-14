# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):

        dummy = ListNode()
        curhead = dummy
        node = head.next
        cursum = 0
        while node and node.next:
            cursum += node.val
            if node.next.val == 0:
                curhead.next = ListNode(cursum)
                curhead = curhead.next
                cursum = 0
            node = node.next
        return dummy.next
