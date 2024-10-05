# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        n = len(s1)
        substring = Counter(s2[:n-1])
        for r in range(n-1,len(s2)):
            substring[s2[r]]+=1
            print(substring)
            if substring == target:
                return True
            substring[s2[r-(n-1)]]-=1
            if substring[s2[r-(n-1)]]==0:
                del substring[s2[r-(n-1)]]
        return False