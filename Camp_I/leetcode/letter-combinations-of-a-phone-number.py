class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        def backtrack(idx,combination):
            if len(combination)==len(digits):
                if digits:
                    copy = "".join(combination)
                    ans.append(copy)
                return
            n = len(hashmap[digits[idx]])
            letter = hashmap[digits[idx]]
            for i in range(n):
                combination.append(letter[i])
                backtrack(idx+1,combination)
                combination.pop()
        backtrack(0,[])
        return ans