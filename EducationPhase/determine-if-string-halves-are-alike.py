class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        fcount = 0
        scount = 0
        vowels = {"a","e","i","o","u"}
        for i in range(len(s)):
            
            if i<(len(s)//2):
                if s[i].lower() in vowels:
                    fcount+=1
            else:
                if s[i].lower() in vowels:
                    scount+=1
        if fcount==scount: return True
        return False