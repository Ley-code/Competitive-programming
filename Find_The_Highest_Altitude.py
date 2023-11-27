class Solution:
    def largestAltitude(self, gain):
        maxalt = 0
        for i in range(len(gain)):
            if i>0:
                gain[i] = gain[i]+gain[i-1]
                maxalt = max(maxalt,gain[i])
            else:
                maxalt = max(maxalt,gain[i])
        return maxalt
