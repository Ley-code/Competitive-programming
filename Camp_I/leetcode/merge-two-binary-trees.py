# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        def recurse(node1,node2):
            if not node1 and node2:
                return node2
            if node1 and not node2:
                return node1
            # if node1.left == None:
            #     node1.left = node2.left
            # if node1.right == None:
            #     node1.right = node2.right
            if node1 and node2:
                node1.val = node1.val+node2.val
                node1.left = recurse(node1.left,node2.left)
                node1.right = recurse(node1.right,node2.right)
            return node1
        return recurse(root1,root2)



