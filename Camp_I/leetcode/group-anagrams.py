class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap ={}
        ans = []
        for word in strs:
            val = str(sorted(word))
            hashmap[val] = hashmap.get(val,[])+[word]       
        for item in hashmap:
            ans.append(hashmap[item])
        return ans