# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        presum = []
        vowels = set(["a","e","i","o","u"])
        for word in words:
            if word[-1] in vowels and word[0] in vowels:
                if not presum:
                    presum.append(1)
                else:
                    presum.append(presum[-1]+1)
            else:
                if not presum:
                    presum.append(0)
                else:
                    presum.append(presum[-1])
        ans = []
        for l,r in queries:
            if l>0:
                ans.append(presum[r]-presum[l-1])
            else:
                ans.append(presum[r])
        return ans