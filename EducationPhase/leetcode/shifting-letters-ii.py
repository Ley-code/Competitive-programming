class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #lettervalues = {ord(c) for c in s}
        presum = [0]*(len(s)+1)
        for start,end,dire in shifts:
            if dire==1:
                presum[start]+=1
                presum[end+1] -=1
            elif dire == 0:
                presum[start]-=1
                presum[end+1]+=1
        for i in range(len(presum)):
            if i>0:
                presum[i] += presum[i-1]
        ans = ""
        for i in range(len(s)):
            order = ord(s[i])+presum[i]-97
            order = order%26
            ans += chr(97+order)
        return ans
