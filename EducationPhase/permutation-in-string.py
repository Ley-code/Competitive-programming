class Solution(object):
    def checkInclusion(self, s1, s2):
        target = Counter(s1)
        sliding_window = Counter(s2[:len(s1)-1])
        l = 0
        r = len(s1)-1
        while r<len(s2):
            sliding_window[s2[r]]+=1
            if target == sliding_window:
                return True
            sliding_window[s2[l]]-=1
            if sliding_window[s2[l]] == 0:
                del sliding_window[s2[l]]
            l+=1
            r+=1
        return False