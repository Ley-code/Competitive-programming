# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        l = 0
        r = len(arr)-1
        maxsum = 0
        while l<r:
            maxsum = max(arr[l]+arr[r],maxsum)
            l+=1
            r-=1
        return maxsum 