class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        r = len(skill)-1
        l = 0
        ans = 0
        target = skill[l] + skill[r] 
        while l<r:
            if skill[l]+skill[r] != target:
                return -1
            else:
                ans+= skill[l]*skill[r]
                l+=1
                r-=1
        return ans