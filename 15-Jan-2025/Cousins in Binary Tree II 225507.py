# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelmap = defaultdict(int)
        queue = deque([root])
        depth = 1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                levelmap[depth]+= node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        queue = deque([root])
        height = 1
        if root:
            root.val = 0
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                sums = 0
                if node.left:
                    sums+= node.left.val
                if node.right:
                    sums +=node.right.val
                if node.left:
                    node.left.val = levelmap[height+1]-sums
                    queue.append(node.left)
                if node.right:
                    node.right.val = levelmap[height+1]-sums
                    queue.append(node.right)
            height+=1
        return root
            