class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        cp = []
        for start,end in nums:
            cp.extend(range(start,end+1))
        up = set(cp)
        return len(up)