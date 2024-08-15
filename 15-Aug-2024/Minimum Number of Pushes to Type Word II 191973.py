# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        keys = 8
        level = 1
        result = list(counts.values())
        result.sort(reverse = True)
        ans = 0
        for val in result:
            if keys==0:
                keys = 8
                level+=1
            ans += (val*level)
            keys-=1
        return ans
