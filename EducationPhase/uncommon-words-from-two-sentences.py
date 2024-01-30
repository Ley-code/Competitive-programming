class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        allsent = s1 + " " + s2
        lists = allsent.split()
        hashmap  = Counter(allsent.split())
        ans = []
        for i in range(len(lists)):
            if hashmap[lists[i]]==1:
                ans.append(lists[i])
        return ans