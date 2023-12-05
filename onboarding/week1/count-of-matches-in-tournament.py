class Solution:
    def numberOfMatches(self, n: int) -> int:
        totalmatches = 0
        while n!=1:
            if n%2==0:
                n = n//2
                totalmatches+=n
            elif n%2!=0:
                matches = (n-1)//2
                n = matches+1
                totalmatches+=matches
        return totalmatches