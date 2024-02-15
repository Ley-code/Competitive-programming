class Solution:
    def longestPalindrome(self, s: str) -> int:
        mp = Counter(s)
        length = 0
        keys = list(mp.keys())
        flag = False
        for key in keys:
            if mp[key]%2!=0:
                length+=mp[key]-1
                flag = True
            else:
                length+=mp[key]
        if flag: 
            length+=1
        return length