class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1,10):
            num = i
            nextnum = i+1
            while num<=high and nextnum<=9:
                num = num*10 + nextnum
                if low<= num <= high:
                    ans.append(num)
                nextnum+=1
        ans.sort()
        return ans