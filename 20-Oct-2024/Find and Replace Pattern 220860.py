# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            hashmap1 = {}
            hashmap2 = {}
            flag = True
            for i in range(len(word)):
                if word[i] in hashmap1:
                    if hashmap1[word[i]]!=pattern[i]:
                        flag = False
                else:
                    hashmap1[word[i]] = pattern[i]
                
                if pattern[i] in hashmap2:
                    if hashmap2[pattern[i]]!= word[i]:
                        flag = False
                else:
                    hashmap2[pattern[i]] = word[i]
            if flag:
                ans.append(word)
        return ans