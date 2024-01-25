class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allup = False
        ssmal = False
        allsmal = False
        if word[0] == word[0].upper():
            if len(word)>1 and word[1]== word[1].lower():
                ssmal = True
            else:
                allup = True
        elif word[0] == word[0].lower():
            allsmal = True
        for i in range(len(word)):
            if allup and word[i]!=word[i].upper():
                return False
            elif allsmal and word[i]!=word[i].lower():
                return False
            elif ssmal and i>0 and word[i]!=word[i].lower():
                return False
        return True
                
                