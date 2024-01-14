class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        target = Counter(word2)
        current = Counter(word1)
        for i in range(len(word1)):
            if word1[i] not in target:
                return False
        one = list(target.values())
        two = list(current.values())
        one.sort()
        two.sort()
        for i in range(len(one)):
            if one[i]!=two[i]:
                return False
        return True