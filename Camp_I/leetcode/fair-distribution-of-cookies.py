class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        best = float('inf')
        split = [0]*k
        def backtrack(pointer):
            nonlocal best
            if pointer==len(cookies):
                best = min(best,max(split))
                return
            for i in range(len(split)):
                if split[i]+cookies[pointer]<best:
                    split[i]+=cookies[pointer]
                    backtrack(pointer+1)
                    split[i]-=cookies[pointer]
        backtrack(0)
        return best