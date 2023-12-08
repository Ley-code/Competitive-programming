class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        for start,end in ranges:
            if  start<=left<=end:
                if start<=right<=end:
                    return True
                else:
                    left=end+1
        return False