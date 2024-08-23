# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        l = 0
        r = 0
        while l<len(firstList) and r<len(secondList):
            if firstList[l][0]<=secondList[r][1] and secondList[r][0]<=firstList[l][1]:
                ans.append([max(firstList[l][0],secondList[r][0]),min(firstList[l][1],secondList[r][1])])
            if firstList[l][1]<=secondList[r][1]:
                l+=1
            else:
                r+=1
        return ans