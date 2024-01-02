class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxval = 0
        for i,num in enumerate(satisfaction): 
            maxval+= (i+1)*num
        for i in range(len(satisfaction)):
            mysum = 0
            for j in range(i,len(satisfaction)):
                if satisfaction[j]<0:
                    mysum+=-satisfaction[j]
                else:
                    mysum-=satisfaction[j]
            maxval = max(maxval,maxval+mysum)
        if maxval<0:
            return 0
        return maxval