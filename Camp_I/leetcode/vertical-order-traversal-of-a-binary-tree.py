# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = {}
        def recurse(node,col,row):
            if not node:
                return
            hashmap[(col,row)] = hashmap.get((col,row),[])+[node.val]
            recurse(node.left,col-1,row+1)
            recurse(node.right,col+1,row+1)
            return
        recurse(root,0,0)
        lists = sorted(list(hashmap.keys()),key = lambda x:(x[0],x[1]))
        mp = defaultdict(list)
        for keys in lists:
            col,row = keys
            mp[col] += sorted(hashmap[keys])
        
        return mp.values()
