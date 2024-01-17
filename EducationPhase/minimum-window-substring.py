class Solution(object):
    def minWindow(self, s, t):
        if t == "": return ""
        window,target = {},{}
        for character in t:
            target[character] = target.get(character,0)+1
        l=0
        res, resLen = [-1,-1],len(s)+1
        need,have = len(target),0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            if s[r] in target and window[s[r]]==target[s[r]]:
                have+=1
            while have == need:
                if (r-l+1)<resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in target and window[s[l]]<target[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != len(s)+1 else "" 