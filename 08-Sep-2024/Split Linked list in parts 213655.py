# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        output = [None]*k
        size = -1
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy
        while curr:
            size+=1
            curr = curr.next
        node = head
        newhead = head
        prevnode = dummy
        const = size//k
        r = size%k
        l = 0
        while node:
            flag = False
            if prevnode.next==None:
                prevnode = node
                flag = True
            for _ in range(const):
                node = node.next
                if flag:
                    flag = False
                    continue
                prevnode = prevnode.next
            print(r)
            if r:
                node = node.next
                if not flag:
                    prevnode = prevnode.next
                flag = False
                r-=1
            prevnode.next = None
            output[l] = newhead
            newhead = node
            l+=1
        return output
