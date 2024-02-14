class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        tot = 0
        while k>0 and numOnes>0:
            tot+=1
            numOnes-=1
            k-=1
        while k>0 and numZeros>0:
            numZeros-=1
            k-=1
        while k>0 and numNegOnes>0:
            tot-=1
            numNegOnes-=1
            k-=1
        return tot