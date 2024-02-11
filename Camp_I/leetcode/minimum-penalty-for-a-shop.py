class Solution:
    def bestClosingTime(self, customers: str) -> int:
        mini = len(customers)+1
        index = -1
        suffix = [0]*(len(customers)+1)
        prefix = [0]*(len(customers)+1)
        count_y = 0
        count_n = 0
        for i in range(len(customers)-1 , -2 ,-1):
            if customers[i] == "Y":
                suffix[i+1] += count_y
                count_y += 1
            else:
                 suffix[i+1] += count_y
        for i in range(len(customers)):
            if customers[i] == "N":
                count_n+=1
                prefix[i+1]+=count_n
            else:
                prefix[i+1] += count_n
        for i in range(len(customers)+1):
            penality = prefix[i]+suffix[i]
            if penality<mini:
                mini = penality
                index = i
        return index
