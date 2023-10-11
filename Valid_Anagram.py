class Solution(object):
    def isAnagram(self, s, t):
        smap = {letter:0 for letter in s}
        tmap = {l:0 for l in t}
        for letter in s:
            smap[letter] +=1
        for l in t:
            tmap[l]+=1
        return True if tmap==smap else False