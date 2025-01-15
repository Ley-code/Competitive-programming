# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        distance = 0
        for i in range(1,len(arrays)):
            distance = max(distance,abs(arrays[i][0]-maxi),abs(arrays[i][-1]-mini))
            maxi = max(maxi,arrays[i][-1])
            mini = min(mini,arrays[i][0])
        return distance