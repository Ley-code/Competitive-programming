class Solution:
    def maxScore(self, s: str) -> int:
        rightsum = 0
        leftsum = 0
        maxsum = 0
        for i in range(len(s)):
            rightsum+=int(s[i])
        for i in range(len(s)):
            if i<(len(s)-1) and s[i] == "0":
                leftsum+=1
            elif s[i] == "1":
                rightsum-=1
            total = rightsum+leftsum
            maxsum = max(total,maxsum)
        return maxsum