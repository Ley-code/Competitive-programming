class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {5:0,10:0}
        take = 0
        for i in range(len(bills)):
            if bills[i]==5:
                hashmap[5]+=1
            elif bills[i]==10:
                hashmap[10]+=1
                hashmap[5]-=1
            if bills[i]==20:
                if hashmap[10]>0:
                    hashmap[10]-=1
                    hashmap[5]-=1
                else:
                    hashmap[5]-=3
            if hashmap[10]<0 or hashmap[5]<0:
                return False
        return True