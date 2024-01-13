class Solution:
    def minSteps(self, s: str, t: str) -> int:
        target = Counter(s)
        word = Counter(t)
        count = 0
        for c in t:
            while c in target and word[c]>target[c]:
                count+=1
                word[c]-=1
            while c not in target and word[c]!=0:
                count+=1
                word[c]-=1
        return count
