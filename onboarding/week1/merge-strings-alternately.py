class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedstring = ""
        l = 0
        mini = min(len(word1),len(word2))

        while l<mini:
            mergedstring+=word1[l]
            mergedstring+=word2[l]
            l+=1
        if mini == len(word1):
            mergedstring+=word2[l:]
        else:
            mergedstring+=word1[l:]
        return mergedstring