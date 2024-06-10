# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freqmap = [0]*(max(heights)+1)
        arr = []
        for height in heights:
            freqmap[height] += 1
        for i,freq in enumerate(freqmap):
            if freq == 0:
                continue
            arr = arr + [i]*freq
        count = 0
        for i in range(len(arr)):
            if arr[i]!= heights[i]:
                count+=1
        return count