class Solution:
    def largestGoodInteger(self, num: str) -> str:
        array = []
     
        for i in range(len(num)):
            if i<len(num)-1 and i>0:
                if num[i+1]==num[i]==num[i-1]:
                    array.extend([int(f"{num[i]}{num[i]}{num[i]}")])
        if array:
            result = max(array)
            if result == 0:
                return "000"
            return f"{result}"
        return ""       
