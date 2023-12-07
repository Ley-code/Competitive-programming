class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersection = set(list1) & set(list2)
        hashmap = {}
        result = []
        for i,word in enumerate(list1):
            if word in intersection:
                hashmap[word] = i
        for j,word in enumerate(list2):
            if word in intersection:
                hashmap[word] += j
        minimum = min(hashmap.values())
        for word,indexsum in hashmap.items():
            if indexsum == minimum:
                result.append(word)
        return result