class Solution(object):
    def firstUniqChar(self, s):
        lettermap = Counter(s)
        for i in range(len(s)):
            if lettermap[s[i]] ==1:
                return i
        return -1

        