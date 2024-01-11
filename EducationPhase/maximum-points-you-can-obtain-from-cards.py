class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length  = len(cardPoints)-k
        if length == 0:
            return sum(cardPoints)
        minisum = float('inf')
        l = 0
        r = length-1
        currsum = sum(cardPoints[:length-1])
        while r<len(cardPoints):
            currsum+=cardPoints[r]
            minisum = min(currsum,minisum)
            currsum-=cardPoints[l]
            l+=1
            r+=1
        return sum(cardPoints)-minisum
