# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0,head)
        curr = head
        while curr:
            newnode = Node(curr.val)
            temp = curr.next
            curr.next = newnode
            newnode.next = temp
            curr = temp
        curr = head
        while curr:
            temp = curr.random
            if not temp:
                curr.next.random = None
            else:
                temp2 = curr.next
                temp2.random = temp.next

            curr = curr.next.next
        curr = head
        prev = dummy
        while curr:
            nextnode = curr.next.next
            prev.next = curr.next
            prev = prev.next
            curr = nextnode
        return dummy.next