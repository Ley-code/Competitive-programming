class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])
        res = 9999
        for i in range(len(fronts)):
            if fronts[i] not in same:
                res = min(res,fronts[i])
            if backs[i] not in same:
                res = min(res,backs[i])
        return res if res!=9999 else 0