class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        rightsum = sum(nums)
        leftsum = 0
        maxsum = rightsum
        ans = []
        n = len(nums)
        for i in range(n+1):
            if i>0 and nums[i-1]==0 :
                leftsum+=1
            currsum = rightsum+leftsum
            if currsum == maxsum:
                ans.append(i)
            elif currsum>maxsum:
                ans = []
                ans.append(i)
                maxsum = currsum
            if i<n and nums[i] == 1:
                rightsum-=1
        return ans
        #summap[currsum] = summap.get(currsum,[])+[]
                 