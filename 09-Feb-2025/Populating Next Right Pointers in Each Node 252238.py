# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        def dfs(node):
            if not node.left and not node.right:
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root