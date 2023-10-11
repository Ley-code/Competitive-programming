import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        r,l = len(s1)-1,0
        target_string = collections.Counter(s1)
        win_string = collections.Counter(s2[:r])
        for i in range(r,len(s2)):
            win_string[s2[i]]+=1
            if target_string == win_string:
                return True
            win_string[s2[l]] -=1
            if win_string[s2[l]] == 0:
                del win_string[s2[l]]
            l+=1
        return False