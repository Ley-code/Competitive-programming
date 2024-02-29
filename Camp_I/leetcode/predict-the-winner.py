class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def maxscore(left,right,turn):
            if left>right:
                return 0
            if turn:
                option1 = nums[left]+maxscore(left+1,right,not turn)
                option2 = nums[right]+maxscore(left,right-1,not turn)
                return max(option1,option2)
            else:
                option1 = -nums[left]+maxscore(left+1,right,not turn)
                option2 = -nums[right]+maxscore(left,right-1,not turn)
                return min(option1,option2)
        score = maxscore(0,len(nums)-1,True)
        return score>=0