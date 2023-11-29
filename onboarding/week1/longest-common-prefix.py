class Solution(object):
    def longestCommonPrefix(self, strs):
        common = ""
        strs.sort()
        left_word,right_word = 0,len(strs)-1
        value = min(len(strs[left_word]),len(strs[right_word]))
        l,r = 0,0
        while l<value and r<value:
            if strs[left_word][l] == strs[right_word][r]:
                common+=strs[left_word][l]
            else:
                break
            l+=1
            r+=1
        return common
        