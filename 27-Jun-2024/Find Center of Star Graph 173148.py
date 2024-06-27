# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        grap = defaultdict(list)
        for n1,n2 in edges:
            if grap[n1]:
                return n1
            if grap[n2]:
                return n2
            grap[n1].append(n2)
            grap[n2].append(n1)
        return -1