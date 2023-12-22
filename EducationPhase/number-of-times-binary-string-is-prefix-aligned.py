class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxi = 0
        count = 0
        for i in range(len(flips)):
            maxi = max(maxi,flips[i])
            if i+1 == maxi:
                count+=1
        return count
