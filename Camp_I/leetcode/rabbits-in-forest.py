class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        nrabit = 0
        info = Counter(answers)
        rabits = list(info.keys())
        for x in rabits:
            val = ceil(info[x]/(x+1))
            nrabit+=(val*(x+1))
        return nrabit
