# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def checkPath(head: ListNode, node: TreeNode) -> bool:
            if not head:
                return True  # Reached the end of the linked list
            if not node:
                return False  # Reached a null tree node but list is not finished
            
            if head.val != node.val:
                return False  # Values don't match
            
            # Recur for both left and right children
            return checkPath(head.next, node.left) or checkPath(head.next, node.right)

        
        if not head:
            return True  # If the linked list is empty, it's trivially a subpath
        if not root:
            return False  # If the tree is empty but the list is not, return False
        
        # Check if starting from this root, we can match the linked list
        if checkPath(head, root):
            return True
        
        # Recur on the left and right subtree
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    




