# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)

        remaining = k%tot

        for i in range(len(chalk)):
            if remaining-chalk[i]<0:
                return i
            remaining -= chalk[i]
        