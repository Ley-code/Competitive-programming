class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        Absent = 0
        for i in range(len(s)):
            if s[i]=="L":
                if count==2:
                    return False
                count+=1
            elif s[i]=="A":
                count = 0
                if Absent == 1:
                    return False
                Absent+=1
            else:
                count = 0
        return True

