# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = len(words)
        for wor in words:
            for c in wor:
                if c not in allowed:
                    count -= 1
                    break
        return count