# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                parent = queue.popleft()
                if parent.right:
                    queue.append(parent.right)
                    graph[parent.val].append(parent.right.val)
                    graph[parent.right.val].append(parent.val)
                if parent.left:
                    queue.append(parent.left)
                    graph[parent.val].append(parent.left.val)
                    graph[parent.left.val].append(parent.val)
        q = deque([target.val])
        visited = set()
        while q and k>0:
            for i in range(len(q)):
                curr = q.popleft()
                visited.add(curr)
                print(graph[curr])
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
            k-=1
        return list(q)

                




                