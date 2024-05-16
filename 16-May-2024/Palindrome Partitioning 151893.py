# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(l,r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        pal = []
        def dp(start,comb):
            if start==len(s):
                pal.append(comb[:])
                return
            for end in range(start,len(s)):
                if ispalindrome(start,end):
                    comb.append(s[start:end+1])
                    dp(end+1,comb)
                    comb.pop()
        dp(0,[])
        return pal
