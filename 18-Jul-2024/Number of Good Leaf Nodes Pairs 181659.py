# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            distances = []
            for d in left_distances:
                if d + 1 <= distance:
                    distances.append(d + 1)
            for d in right_distances:
                if d + 1 <= distance:
                    distances.append(d + 1)
            
            return distances
        
        dfs(root)
        return self.result