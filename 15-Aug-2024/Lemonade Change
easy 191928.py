# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = defaultdict(int)
        for bill in bills:
            if bill==5:
                cash[5]+=1
            elif bill==10:
                if cash[5]==0:
                    return False
                cash[10]+=1
                cash[5]-=1
            else:
                if cash[10] and cash[5]:
                    cash[10]-=1
                    cash[5]-=1
                elif cash[5]>=3:
                    cash[5]-=3
                else:
                    return False
        return True



