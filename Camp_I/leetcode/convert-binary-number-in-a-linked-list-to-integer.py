# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(str(curr.val))
            curr = curr.next
        binary = "".join(arr)
        binary = binary[::-1]
        ans = 0
        for i in range(len(binary)):
            if binary[i]=="1":
                ans+= 2**i
        return ans

    